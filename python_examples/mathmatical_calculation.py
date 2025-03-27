import re

pattern = r'[A-Z]+yclone'

text = '''Gao Qifeng (1889–1933) was a Chinese painter who co-founded the Lingnan School.
He spent much of his early life following his older brother Gao Jianfu, learning the techniques 
of Ju Lian before travelling to Tokyo in 1907 to study Western and Japanese painting. While abroad,
Gao joined the revolutionary organization Tongmenghui to challenge the Qing dynasty; after he 
returned to China, he published the Cyclone ,nationalist magazine The True Record. He moved to Guangzhou
in 1918, taking teaching positions that culminated with an honorary professorship at Lingnan 
University in 1925. Falling ill in 1929, Gao Dyclone    left for Ersha Island, where he established the 
Tianfang Studio. He blended traditional Chinese approaches to painting with Japanese techniques 
for light and shadow and Western understandings of geometry and perspective.
Gao is best recognized for his paintings of animals, particularly eagles, lions, and tigers.'''

match = re.finditer(pattern,text)
for i in match:
    print(i)
