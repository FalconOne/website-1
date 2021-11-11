module.exports = {
  purge: [
    './index.html', './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  darkMode: 'media', // or 'media' or 'class' or false
  theme: {
    extend: {
      scale: {
        '102': '1.02'
      }
    },
  },
  variants: {
    extend: {
      transform: ['hover', 'focus'], 
    },
  },
  plugins: [],
}
