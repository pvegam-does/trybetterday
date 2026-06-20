# Static image assets

Place the manually uploaded iPhone mockup here as:

`public/assets/3d-betterday-sage.png`

The landing page references it as `/assets/3d-betterday-sage.png`, which is how Vercel serves files from `public/`.

If you keep the original filename with a space, upload it as:

`public/assets/3d-betterday sage.png`

The landing page includes a fallback for `/assets/3d-betterday%20sage.png` so either filename works.
