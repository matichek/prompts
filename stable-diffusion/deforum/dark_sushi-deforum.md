
## base prompt:

Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, ((streamer room)), headset, 1girl, woman, curly long hair, (red dress), anime, beautiful, brown hair, beautiful brown eyes, makeup, flat chest, closed mouth, halftone, background monstera plant garden, gamer chair, particles, bokeh, double exposure, (original illustration composition), (fusion of limited color, maximalism artstyle, geometric artstyle, Swiss cheese plant, junk art), <lora:add_detail:0.6> 
Negative prompt: 2girl, easynegative, ng_deepnegative_v1_75t, (worst quality:2), (low quality:2), bad-hands-5, (cleavage), (big chest ), nsfw
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 2871189008, Size: 912x512, Model hash: cca17b08da, Clip skip: 2, Lora hashes: "add_detail: 7c6bad76eb54", Version: v1.3.2



Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, ((streamer room)), headset, 1girl, woman, curly long hair, (red dress), anime, beautiful, brown hair, beautiful brown eyes, makeup, flat chest, closed mouth, halftone, background monstera plant garden, gamer chair, particles, bokeh, double exposure, (original illustration composition), (fusion of limited color, maximalism artstyle, geometric artstyle, Swiss cheese plant, junk art), <lora:add_detail:0.6> 

### Deforum test anim

{
    "0": "Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, ((streamer room)), headset, 1girl, woman, curly black long hair, (red dress), anime, beautiful, beautiful brown eyes, makeup, flat chest, closed mouth, halftone, background monstera plant garden, gamer chair, particles, bokeh, double exposure, (original illustration composition), (fusion of limited color, maximalism artstyle, geometric artstyle, Swiss cheese plant, junk art), <lora:add_detail:0.6>",
    "15": "Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, ((streamer room)), headset, 1girl, woman, curly black long hair, (red dress), anime, beautiful, beautiful brown eyes, makeup, flat chest, closed mouth, halftone, background monstera plant garden, gamer chair, particles, bokeh, double exposure, (original illustration composition), (fusion of limited color, maximalism artstyle, geometric artstyle, Swiss cheese plant, junk art), <lora:add_detail:0.6>"
}

- beware of backslashes - not forward slashes

D:/Premier/Projects/davinci/test.mp4

With all those extension - I get errors if I run Defoum + ControlNet

V1
To get stable results:
- SubSeed
- Seed - fixed
- Choose Seed in prompt


## Video animation for video - "Choose" audio project - Matichek

time: 251s
frames: 15060

Part 1 close up shot

No ControlNet, only video input

Test:
Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, woman, 1girl, curly black hair, anime, geometric artstyle, junk art
Negative prompt: easynegative, bad-picture-chill-75v, nude, nsfw, blurry
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1993765611, Size: 768x512, Model hash: cca17b08da, Denoising strength: 0.5, Clip skip: 2, Version: v1.4.0

Used embeddings: easynegative [119b], bad-picture-chill-75v [1eff]


{
    "0": "Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, woman, 1girl, beautiful green eyes, curly black hair, anime, geometric artstyle, junk art",
    "690": "Ambilight, masterpiece, ultra-high quality, (ultra detailed original illustration), octans, woman, 1girl, beautiful green eyes, curly black hair, anime, geometric artstyle, junk art"
}


test2:
D:/Premier/Projects/davinci/choose-video/test2.mp4