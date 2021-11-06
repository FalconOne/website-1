module.exports = {
  purge: [
    './index.html', './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  darkMode: 'media', // or 'media' or 'class' or false
  theme: {
    extend: {},
  },
  variants: {
    extend: {
      transform: ['hover', 'focus'], 
    },
  },
  plugins: [],
}
