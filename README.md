# YouSum 

`yousum` is a command-line tool that downloads audio from YouTube videos, transcribes them, and generates summaries. It uses Whisper and GPT to deliver accurate transcriptions and summaries in a user-friendly format.

## Quickstart

-  `pip install git+https://github.com/padiauj/yousum.git`
-  `yousum [URL]`



## Installation

### Requirements

- Python 3.7 or higher
- OpenAI key, preferably stored in the standard environment variable `OPENAI_API_KEY`


## Usage
```
usage: yousum [-h] [-m MODEL] [-p PROMPT] [-s SYS_PROMPT] [-o OUTDIR] url

yousum - summarize youtube videos with GPT and Whisper

positional arguments:
  url                   url of youtube video to summarize

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Model to use for summarization (default: gpt-3.5-turbo)
  -p PROMPT, --prompt PROMPT
                        Custom summarization prompt
  -s SYS_PROMPT, --sys_prompt SYS_PROMPT
                        Custom system prompt for summarization
  -o OUTDIR, --outdir OUTDIR
                        Where to output transcription and summary
```
Just Run:

`pip install git+https://github.com/padiauj/yousum.git`


## License

`yousum` is licensed under the [MIT License](LICENSE.md).
