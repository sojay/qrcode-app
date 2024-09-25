/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'mono': ['IBM Plex Mono', 'Noto Sans Mono Variable', 'monospace'],
        'sans': ['Noto Sans Mono', 'monospace'],
      }
    },
  },
  plugins: [],
}

