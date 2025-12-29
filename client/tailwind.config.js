/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'umaja-dark': '#0a0a0a',
        'umaja-gold': '#d4af37',
        'umaja-blue': '#1e40af',
      },
    },
  },
  plugins: [],
}
