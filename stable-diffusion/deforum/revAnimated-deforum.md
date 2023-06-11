# Template for the video description

{
    "0": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "30": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "60": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "90": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "150": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "240": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "350": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
    "480": "masterpiece, ___________ epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art"
}

## Settings
 
strength schedule:
0: (0.65),  25: (0.55)
translation x
0:(0), 30:(15), 210:(15), 300:(0)
translation y
0:(0)
translation z
0:(0.2), 60:(10), 300:(15)
rotation 3d x
0:(0), 60:(0), 90:(0.5), 180:(0.5), 300:(0.5)
rotation 3d y
0:(0), 30:(-3.5), 90:(-2.5), 180:(-2.8), 300:(-2), 420:(0)
rotation 3d z
0:(0), 60:(0.2), 90:(0), 180:(-0.5), 300:(0), 420:(0.5), 500:(0.8)
 
- FOV -
0:(120)
 
-Noise TAB - 
noise schedule:
0:(-0.06*(cos(3.141*t/15)**100)+0.06)
 
- ANTI-BLUE TAB -
amount schedule
0: (0.05)


# Test video 

600 frames

{
"0": "masterpiece, astronauts, holding a reward, explotion of colors, spaceship in the background, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"30": "masterpiece, astronauts, walking on the alien planet, looking at the glowing sphere, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"60": "masterpiece, astronauts, walking into the portal, galaxy, mystery, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"90": "masterpiece, astronauts, finding the magic cube, glowing blue, beautiful landspace, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"150": "masterpiece, astronauts, walking into the beautiful portal, glowing, heaven light, pyramids, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"240": "masterpiece, astronauts, finding tresure, mountain in the distant, glowing light in the peak, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"350": "masterpiece, astronout, landing on the planet Earth, calm, desert scene, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art",
"480": "masterpiece, astronauts, drinking coffee and relaxing, epic scene, vibrant colors, full hd, full body, dynamic lighting, ultra-high detail, dramatic lighting, movie poster style, asymmetric composition, photorealistic, unreal engine, concept art"
}

10s - 15fps - 150frames

### anything-v4.0

1girl, outdoors, viewing sunrise, viewing back, drinking coffee, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic
Negative prompt: easynegative, lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts)), (monochrome:1.1), lie, hands upmited palett
Steps: 86, Sampler: Euler a, CFG scale: 7, Seed: 1371371373, Size: 1024x1024, Model hash: 3b26c9c497, Denoising strength: 0.36, Clip skip: 2, Ultimate SD upscale upscaler: RealESRGAN_x4plus_anime_6B, Ultimate SD upscale tile_width: 512, Ultimate SD upscale tile_height: 512, Ultimate SD upscale mask_blur: 8, Ultimate SD upscale padding: 32, ControlNet 0: "preprocessor: tile_resample, model: control_v11f1e_sd15_tile [a371b31b], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (64, 1, 64)"

{
    "0": "1girl, outdoors, viewing sunrise, viewing back, drinking coffee, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic",
    "30": "1girl, outdoors, viewing sunrise, standing up, viewing back, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic",
    "60": "1girl, outdoors, viewing sunrise, walking, outside, park, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic",
    "90": "1girl, outdoors, evening, walking, park, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic",
    "120": "1girl, outdoors, night, walking, park, brown hair, beautiful, cute, city, mountains, nekomimi, photorealistic, fluffy clouds, photorealistic environment, cinematic, 8k, fisheye lens, (girl focus), photorealism, realistic"
}

Negative prompt:
nsfw, nude,  easynegative, lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, low quality, normal quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts)), (monochrome:1.1), lie, hands upmited palett

### "Dark sushi Mix" test
https://civitai.com/models/24779/dark-sushi-mix-mix

* Generated video:
https://www.youtube.com/shorts/MVdA_yu-WsA

Main prompt:
octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone,cloud, light_particles, space, sky,water,girl,night
Negative prompt: 2girl,(EasyNegative)，(((simple background))),monochrome ,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, lowres, bad anatomy, bad hands, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, ugly,pregnant,vore,duplicate,morbid,mut ilated,tran nsexual, hermaphrodite,long neck,mutated hands,poorly drawn hands,poorly drawn face,mutation,deformed,blurry,bad anatomy,bad proportions,malformed limbs,extra limbs,cloned face,disfigured,gross proportions, (((missing arms))),(((missing legs))), (((extra arms))),(((extra legs))),pubic hair, plump,bad legs,error legs,username,blurry,bad feet
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 3380870324, Size: 768x512, Model hash: cca17b08da, Model: MAADBD2fp16, Denoising strength: 0.5, Clip skip: 2, Wildcard negative prompt: "2girl,(EasyNegative)，(((simple background))),monochrome ,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, lowres, bad anatomy, bad hands, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, ugly,pregnant,vore,duplicate,morbid,mut ilated,tran nsexual, hermaphrodite,long neck,mutated hands,poorly drawn hands,poorly drawn face,mutation,deformed,blurry,bad anatomy,bad proportions,malformed limbs,extra limbs,cloned face,disfigured,gross proportions, (((missing arms))),(((missing legs))), (((extra arms))),(((extra legs))),pubic hair, plump,bad legs,error legs,username,blurry,bad feet", Hires upscale: 2, Hires steps: 20, Hires upscaler: Latent, Version: v1.3.2

{
    "0": "octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone,cloud, light_particles, space, sky,water,girl,night",
    "30": "octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone, cloud, light_particles, space, sky, water,girl,night",
    "60": "octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone, cloud, light_particles, space, sky, water,girl,night",
    "90": "octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone, cloud, light_particles, space, sky, water,girl,night",
    "120": "1octans, sky, star (sky), scenery, starry sky, night, 1girl, night sky, solo, outdoors, signature, building, cloud, milky way, sitting, tree, long hair, city, silhouette, cityscape，masterpiece, best quality, ,halftone, cloud, light_particles, space, sky, water,girl,night"
}





# Based on reference video

## Research - reddit

---

https://www.reddit.com/r/StableDiffusion/comments/12y7z7i/tiktok_girls_hot_dancing/

I guess this kind of style would be idea - feels very organic and drawn. 

* Chika dance
(is this rotoscopping - - 3d animations made more choppy to look like anime 2d animation?)

https://v.animethemes.moe/KaguyaSamaWaKokurasetai-ED2-NCBD1080.webm

Most of my animations turn out so varied LOL. I would love to know how OP keeps consistency in the clothing (and everything). My attempt is not to replicate exactly what OP is doing but just get a consistent start somewhere. This is the workflow:

DarkSushi25D (Also tried Dark Sushi v1) > Mov2Mov > prompt: masterpiece, best quality, anime - Negative: bad-hands-5, easynegative, verybadimagenegative_v1.3, (low quality, worst quality:1.3)

Settings:
CFG: 4 Denoise: 0.2 Movie Frames: 29.97 (It takes forever to render) Sampler: DDIM Seed is consistent (not -1)
ControlNet 1.1.107 (Assume v1.1 pth and yaml files for all)
ControlNet 0 - Softedge_pidinet > Softedge - weight 1 Guess Mode: Balanced
ControlNet 1 - Openpose > openpose - weight 1 Guess Mode: Controlnet is more important
ControlNet 2 - Canny > canny - weight 0.4 (full weight of 1 seems worse results) Guess Mode: controlnet is more important

I've tried varying combinations of controlnet settings, only using canny, only using open pose, using openpose with softedge (the new HED), with little consistency in results. Short of training a LORA for each video (my 3080 doesn't seem to be able to process using dreambooth due to lack of memory, 12GB VRAM), I'm not sure how to get the clothes from changing so often.
Any thoughts or feedback would be so appreciated.

PS. OP your new "sketch" style video on YT from today is so great! Even if you don't want to share your workflow, it is still very much appreciated to see the new work and hope you keep doing what you're doing.

* flickering issues

I appreciate the feedback and will try it with 4 using your suggestions.
Re: flicker, if you have Davinci Resolve Studio, you can do the deflicker fusion a la Corridor Labs walkthrough. 
If not, something I discovered that was pretty interesting was duplicating the sequence in your video app (I'm using Resolve - sans Studio), then putting it on top of the original sequence, moving it over a single frame, then using a Darken composite at 50%. 
For walkthrough of that process and have clipped it from the starting point where he discusses this, see here: https://youtu.be/kmT-z2lqEPQ?t=1669


Demo ref video:
https://www.pexels.com/video/a-female-dancer-showing-her-dance-moves-5385878/

revAnimated rules:

Order matters - words near the front of your prompt are weighted more heavily than the things in the back of your prompt.
Prompt order - content type > description > style > composition
This model likes: ((best quality)), ((masterpiece)), (detailed) in beginning of prompt if you want anime-2.5D type
This model does great on PORTRAITS

img2img - tile scale 2x

Grab all frames as png:
https://www.youtube.com/watch?v=y5PGve7BqFc&t=59s






---

