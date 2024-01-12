import simpleaudio as sa

if __name__ == '__main__':
    sa.WaveObject.from_wave_file('info.wav').play().wait_done()
