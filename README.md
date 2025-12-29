# CommunityApp - UMAJA OMEGA CORE

UMAJA OMEGA CORE v2.2.0-STABLE - A simulation backend with Express, TypeScript, CORS, and HDC/81-19 protocol.

## Prerequisites

- Node.js (v18 or higher recommended)
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
  - Includes HDC efficiency (12-28% range) and 81/19 protocol split

## Features

- **Express Server**: Fast, unopinionated web framework
- **TypeScript**: Type-safe development
- **CORS Enabled**: Configured for frontend at `http://localhost:3000`
- **Simulation Protocols**:
  - HDC Resonance (12-28% efficiency)
  - 81/19 Protocol (Architect/Justice split)

## Development

The server uses `ts-node` with ESM loader for TypeScript execution. Changes to source files will require restarting the server.

## Version

Current version: **2.2.0-STABLE**

## License

[Add license information here]
