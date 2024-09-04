# yt2mp3
YouTube to MP3

## Setup

```bash
cp -p src/data.py.example src/data.py
```

## Run

```bash
python src/run.py
```

```bash
ls output/*.mp3
```

```bash
ls output/*.mp3 | wc -l
```

## Adjust audio volume

```bash
python src/adjust_audio_volume.py
```

```bash
ls output_adjusted/*.mp3
```

```bash
ls output_adjusted/*.mp3 | wc -l
```

## data.py maker

[Generate data.py using YouTube API #3](https://github.com/wasabina67-org/yt2mp3/issues/3)

```bash
python src/data_py_maker.py
```

## mkdocs

```bash
mkdocs serve
```

```bash
mkdocs gh-deploy
```
