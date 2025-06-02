// uno.config.ts
import {
  defineConfig,
  presetUno,
  presetAttributify,
  presetIcons,
  presetWind,
} from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons(),
    presetWind(),
  ],
  theme: {
    colors: {
      softblue: {
        50:  '#f0f7ff',
        100: '#d9ecff',
        200: '#b3d9ff',
        300: '#85c2ff',
        400: '#57aaff',
        500: '#2a92ff',
        600: '#007aff',
        700: '#0063d1',
        800: '#004ca3',
        900: '#003575',
      },
    },
  },
})
