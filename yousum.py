import argparse
from pytube import YouTube
import os
from io import BytesIO
import openai
import tempfile
import sys
import logging
from pytube.exceptions import RegexMatchError

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

SUMMARIZER_SYSTEM_PROMPT = "You are a helpful assistant that summarizes transcriptions."
SUMMARIZER_PROMPT_PREFIX = "Summarize the following transcription of a Youtube video: "


def get_audio(url: str):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    fp = tempfile.NamedTemporaryFile(suffix=".mp3")
    video.stream_to_buffer(buffer=fp)
    fp.seek(0)
    return fp


def transcribe(bio) -> str:
    return openai.Audio.transcribe("whisper-1", bio)["text"]


def summarize(text: str):
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": SUMMARIZER_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": SUMMARIZER_PROMPT_PREFIX + text,
            },
        ],
    )
    return result["choices"][0]["message"]["content"]


def summarize_youtube(url: str) -> str:
    logger.debug("Downloading... ")
    bio = get_audio(url)
    logger.debug("Transcribing... ")
    text = transcribe(bio)["text"]
    logger.debug("Summarizing... ")
    summary = summarize(text)
    return summary
