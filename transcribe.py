import sys
import json
import whisper

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No audio file path provided"}))
        return

    audio_path = sys.argv[1]

    try:
        # Load Whisper model (downloads once and then caches)
        model = whisper.load_model("small")  # or "small.en"
        result = model.transcribe(audio_path)

        print(json.dumps({"text": result.get("text", "")}, ensure_ascii=False))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
