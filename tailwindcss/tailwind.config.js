const plugin = require('tailwindcss/plugin')
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        appBlue: "#1d4ed8",
      },
    },
    variants: {
      extend: {},
    },
    plugins: [require('@tailwindcss/forms'), require('daisyui')],
  }
}
