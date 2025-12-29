# CommunityApp - UMAJA OMEGA CORE

UMAJA OMEGA CORE v2.2.0-STABLE - A simulation backend with Express, TypeScript, CORS, and HDC/81-19 protocol.

## About the Simulation

This application simulates two key protocols:

- **HDC (Harmonic Distribution Coefficient)**: Represents resonance efficiency measurements ranging from 12-28%
- **81/19 Protocol**: A balanced allocation system with an 81% architect component and 19% justice component

## Prerequisites

- Node.js (v18 or higher)
- npm (comes with Node.js)
- Git

## Getting Started

Follow these steps to set up your development environment:

### 1. Clone the Repository

```bash
git clone https://github.com/harrie19/CommunityApp.git
cd CommunityApp
```

### 2. Switch to Main Branch

```bash
git checkout main
git pull origin main
```

### 3. Install Dependencies

```bash
npm install
```

### 4. Run the Development Server

```bash
npm run dev
```

The server will start on `http://localhost:8080`. You can verify it's running by visiting:
- Health endpoint: `http://localhost:8080/health`

## Project Structure

```
.
├── src/
│   ├── server.ts       # Main server entry point
│   ├── app.ts          # Application configuration
│   ├── env.ts          # Environment variables
│   └── routes/         # API routes
├── package.json        # Node.js dependencies and scripts
├── tsconfig.json       # TypeScript configuration
└── README.md          # This file
```

## Available Scripts

- `npm run dev` - Start the development server with hot reload

## API Endpoints

### Health Check
- **GET** `/health`
  - Returns server status, version, and protocol information
  - Includes HDC (Harmonic Distribution Coefficient) efficiency reading in the 12-28% range
  - Includes 81/19 protocol split showing architect (81%) and justice (19%) allocation

## Features

- **Express Server**: Fast, unopinionated web framework
- **TypeScript**: Type-safe development
- **CORS Enabled**: Configured for frontend at `http://localhost:3000`
- **Simulation Protocols**:
  - **HDC Resonance**: Harmonic Distribution Coefficient with 12-28% efficiency range
  - **81/19 Protocol**: Balanced allocation system (81% Architect / 19% Justice)

## Development

The server uses `ts-node` with ESM loader for TypeScript execution. Changes to source files will require manually restarting the server. Hot reload functionality can be added with additional tooling if needed (e.g., nodemon).

## Version

Current version: **2.2.0-STABLE**
