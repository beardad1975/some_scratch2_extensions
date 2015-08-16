#!/usr/bin/env python3

import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


SVSFDefault = 0
SVSFlagsAsync = 1

speaker.Volume = 100
speaker.Rate = 0

s = "S Four A蘇老師人人誇，熱心投入創客教育，指導學生非常用心"



speaker.Speak("測試一，語音等待測試")
speaker.Speak(s, SVSFDefault)
print ("此段文字在語音結束後印出")

time.sleep(2)

speaker.Speak("測試二，語音不等待測試")

speaker.Speak(s, SVSFlagsAsync)
print ("此段文字與語音同時印出")

speaker.WaitUntilDone(-1)

time.sleep(2)


speaker.Speak("測試三，語音音量測試，分為大、中、小")

speaker.Volume = 100
speaker.Speak("S Four A蘇老師人人誇", SVSFDefault)
speaker.Volume = 85
speaker.Speak("熱心投入創客教育", SVSFDefault)
speaker.Volume = 70
speaker.Speak("指導學生非常用心", SVSFDefault)

time.sleep(2)
speaker.Volume = 100

speaker.Speak("測試四，語音速度測試，分為中、快、慢")
speaker.Rate = 0
speaker.Speak("S Four A蘇老師人人誇", SVSFDefault)
speaker.Rate = 6
speaker.Speak("熱心投入創客教育", SVSFDefault)
speaker.Rate = -9
speaker.Speak("指導學生非常用心", SVSFDefault)

speaker.WaitUntilDone(-1)
