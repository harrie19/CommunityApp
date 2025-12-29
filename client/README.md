# UMAJA OMEGA CORE Frontend Dashboard

Real-time monitoring dashboard for the UMAJA OMEGA CORE simulation backend.

## Features

- 🔄 **Real-time Updates**: Polls backend health endpoint every 2 seconds
- 📊 **HDC Visualization**: Progress bar showing Harmonic Distribution Coefficient (12-28%)
- ⚖️ **81/19 Protocol Display**: Visual cards and pie chart for allocation split
- 🌙 **Dark Mode Design**: Black/Gold/Blue color scheme
- 📱 **Fully Responsive**: Works perfectly on desktop and mobile devices
- ✨ **Modern Stack**: Vite + React + TypeScript + Tailwind CSS

## Prerequisites

- Node.js (v18 or higher)
- Backend server running on port 8080

## Getting Started

### 1. Install Dependencies

```bash
cd client
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The dashboard will be available at `http://localhost:5173` (or another port if 5173 is in use).

## Usage

1. Start the backend server first (from the root directory):
   ```bash
   npm run dev
   ```

2. In a new terminal, start the frontend:
   ```bash
   cd client
   npm run dev
   ```

3. Open your browser to the URL shown in the terminal (usually `http://localhost:5173`)

## Dashboard Components

### Status Display
- Shows HEALTHY/OFFLINE status with animated indicator
- Displays last update timestamp
- Shows error messages if backend is unreachable

### HDC Resonance Card
- Color-coded progress bar (red/orange/yellow/gold/green)
- Shows current efficiency percentage
- Displays min (12%), current, and max (28%) values

### Huqúqu'lláh Protocol Card
- Architect (81%) and Justice (19%) allocation cards
- Visual progress bars for each component
- Pie chart visualization of the split
- Compliance status indicator

## Configuration

The frontend expects the backend to be running at `http://localhost:8080/health`. If you need to change this, modify the fetch URL in `src/App.tsx`.

## Build for Production

```bash
npm run build
```

The build output will be in the `dist` directory.

## Technologies

- **Vite**: Fast build tool and dev server
- **React 18**: UI library
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **@tailwindcss/postcss**: Modern PostCSS integration

## Troubleshooting

### Backend Connection Error
If you see "Backend nicht erreichbar" message:
- Ensure the backend server is running on port 8080
- Check that there are no CORS issues
- Verify the backend URL in App.tsx

### Port Already in Use
If port 5173 is in use, Vite will automatically try the next available port. Check the terminal output for the actual URL.
