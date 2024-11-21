from auralis import TTS, TTSRequest

tts = TTS(scheduler_max_concurrency=12).from_pretrained("AstraMindAI/xttsv2", device='cuda:1')

request = TTSRequest(
    text="愛しい彼女へ "
         "あなたの笑顔は私の人生を照らす光です。"
         "毎日あなたと過ごせることが私の幸せです。"
         "あなたは私の心の中で一番大切な人です。"
         "いつも一緒にいてくれて、"
         "ありがとう。"
         "愛を込めて",
    language="ja",
    speaker_files=["/home/marco/Musica/marco_speaking.ogg"],
)

output = tts.generate_speech(request)

output.play()