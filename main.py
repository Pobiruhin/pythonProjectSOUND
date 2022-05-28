import numpy as np
import simpleaudio as sa

frequency = 174 # Наша сыгранная нота будет 174 Гц

def soundTrack():
    fs = 44100  # 44100 выборок в секунду
    seconds = 1  # Примечание длительность 3 секунды
# Генерировать массив с секундами * сэмплированием шагов, в диапазоне от 0 до 3 секунд
    t = np.linspace(0, seconds, seconds * fs, False)
# Генерация синусоидальной волны 440 Гц
    note = np.sin(frequency * t * 2 * np.pi)
# Убедитесь, что максимальное значение находится в 16-битном диапазоне
    audio = note * (2**15 - 1) / np.max(np.abs(note))
# Конвертировать в 16-битные данные
    audio = audio.astype(np.int16)
# Начать воспроизведение
    play_obj = sa.play_buffer(audio, 1, 2, fs)
# Дождитесь окончания воспроизведения перед выходом
    play_obj.wait_done()

soundTrack()

