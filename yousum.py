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

def get_audio(url): 
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    fp = tempfile.NamedTemporaryFile(suffix=".mp3")
    video.stream_to_buffer(buffer=fp)
    fp.seek(0)
    return fp

def transcribe(bio):
    return openai.Audio.transcribe("whisper-1", bio)

def summarize(text):
    result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes transcriptions."},
            {"role": "user", "content": "Summarize the following transcription of a Youtube video: " + text},
        ]
    )
    return result["choices"][0]["message"]["content"]

def summarize_youtube(url): 
    logger.debug("Downloading... ")
    bio = get_audio(url)
    logger.debug("Transcribing... ")
    text = transcribe(bio)["text"]
    logger.debug("Summarizing... ")
    summary = summarize(text)
    return summary 
