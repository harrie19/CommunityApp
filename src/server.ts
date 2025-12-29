import { app } from './app.js';
import { env } from './env.js';

const server = app.listen(env.PORT, () => {
  console.log(`🛡️  UMAJA-CORE AKTIV AUF PORT ${env.PORT}`);
  console.log('⚖️  Huqúqu\'lláh-Protokoll: Aktiv (81/19)');
});

process.on('SIGTERM', () => {
  console.log('UMAJA: Graceful shutdown');
  server.close();
});
