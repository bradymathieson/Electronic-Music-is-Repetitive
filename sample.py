import nltk

cascada_lyrics = """
[Verse 1]
I still hear your voice, when you sleep next to me
I still feel your touch in my dream
Forgive me my weakness, but I don't know why
Without you it's hard to survive

[Chorus]
Cause everytime we touch, I get this feeling
And everytime we kiss, I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side
Cause everytime we touch, I feel the static
And everytime we kiss, I reach for the sky
Can't you hear my heart beat so...
I can't let you go
Want you in my life

[Verse 2]
Your arms are my castle, your heart is my sky
They wipe away tears that I cry
The good and the bad times, we've been through them all
You make me rise when I fall

[Chorus]
Cause everytime we touch, I get this feeling
And everytime we kiss, I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side
Cause everytime we touch, I feel the static
And everytime we kiss, I reach for the sky
Can't you hear my heart beat so...
I can't let you go
Want you in my life

[Outro]
Cause everytime we touch, I get this feeling
And everytime we kiss, I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side
"""

def main():
    tokens = nltk.word_tokenize(cascada_lyrics)
    print(tokens[:10])

if __name__ == '__main__':
    main()
