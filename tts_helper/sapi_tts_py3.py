#!/usr/bin/env python3
"""
Created on Sun Aug  16 7:49:15 2015
@author: Wen-Hung , Chang
Copyright (c) 2015 Wen-Hung, Chang All right reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""




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
