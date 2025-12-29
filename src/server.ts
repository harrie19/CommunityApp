import { app } from './app.js';
import { env } from './env.js';

const server = app.listen(env.PORT, () => {
  console.log(`\n🛡️  UMAJA-CORE AKTIV AUF PORT ${env.PORT}`);
  console.log(`⚖️  Huqúqu'lláh-Protokoll stabilisiert: ${env.SPLIT_ARCHITECT}/${env.SPLIT_JUSTICE}`);
  console.log(`🚀 System bereit für HDC-Resonanz.\n`);
});

process.on('SIGTERM', () => {
  console.log('UMAJA: Graceful shutdown initiated');
  server.close();
});
