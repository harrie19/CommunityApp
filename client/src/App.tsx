import { useState, useEffect } from 'react';
import './App.css';

interface HealthData {
  status: string;
  mode: string;
  version: string;
  timestamp: string;
  protocols: {
    hdc: {
      efficiency: number;
      unit: string;
      target: string;
    };
    huququh: {
      architect: number;
      justice: number;
      compliant: boolean;
    };
  };
}

function App() {
  const [healthData, setHealthData] = useState<HealthData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdate, setLastUpdate] = useState<Date>(new Date());

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const response = await fetch('http://localhost:8080/health');
        if (!response.ok) throw new Error('Backend nicht erreichbar');
        const data = await response.json();
        setHealthData(data);
        setError(null);
        setLastUpdate(new Date());
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unbekannter Fehler');
      }
    };

    // Initial fetch
    fetchHealth();

    // Poll every 2 seconds
    const interval = setInterval(fetchHealth, 2000);

    return () => clearInterval(interval);
  }, []);

  const getHDCColor = (efficiency: number) => {
    if (efficiency < 15) return 'from-red-500 to-orange-500';
    if (efficiency < 20) return 'from-orange-500 to-yellow-500';
    if (efficiency < 25) return 'from-yellow-500 to-umaja-gold';
    return 'from-umaja-gold to-green-500';
  };

  const hdcPercentage = healthData 
    ? ((healthData.protocols.hdc.efficiency - 12) / 16) * 100 
    : 0;

  return (
    <div className="min-h-screen bg-gradient-to-br from-umaja-dark via-gray-900 to-umaja-dark p-4 md:p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <header className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-umaja-gold to-umaja-blue mb-2">
            UMAJA OMEGA CORE
          </h1>
          <p className="text-gray-400 text-sm">
            Version {healthData?.version || '...'} • {healthData?.mode || 'LOADING'}
          </p>
        </header>

        {/* Status Card */}
        <div className="mb-6">
          <div className={`rounded-xl p-6 border-2 ${
            healthData?.status === 'HEALTHY' 
              ? 'bg-green-900/20 border-green-500' 
              : error 
                ? 'bg-red-900/20 border-red-500'
                : 'bg-gray-800/50 border-gray-600'
          }`}>
            <div className="flex items-center justify-between flex-wrap gap-4">
              <div className="flex items-center gap-3">
                <div className={`w-4 h-4 rounded-full ${
                  healthData?.status === 'HEALTHY' 
                    ? 'bg-green-500 animate-pulse' 
                    : error 
                      ? 'bg-red-500'
                      : 'bg-gray-500'
                }`}></div>
                <span className="text-2xl md:text-3xl font-bold">
                  {error ? 'OFFLINE' : healthData?.status || 'CONNECTING...'}
                </span>
              </div>
              <div className="text-sm text-gray-400">
                Letzte Aktualisierung: {lastUpdate.toLocaleTimeString('de-DE')}
              </div>
            </div>
            {error && (
              <div className="mt-4 text-red-400 text-sm">
                ⚠️ {error} - Stellen Sie sicher, dass der Backend-Server läuft (npm run dev)
              </div>
            )}
          </div>
        </div>

        {healthData && (
          <div className="grid md:grid-cols-2 gap-6">
            {/* HDC Efficiency Card */}
            <div className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700 hover:border-umaja-blue transition-colors">
              <div className="flex items-center gap-2 mb-4">
                <div className="w-3 h-3 bg-umaja-blue rounded-full"></div>
                <h2 className="text-xl font-semibold text-umaja-blue">HDC Resonance</h2>
              </div>
              
              <div className="mb-4">
                <div className="flex justify-between items-baseline mb-2">
                  <span className="text-sm text-gray-400">Harmonic Distribution Coefficient</span>
                  <span className="text-sm text-gray-500">{healthData.protocols.hdc.target}</span>
                </div>
                
                <div className="relative h-8 bg-gray-700 rounded-full overflow-hidden">
                  <div 
                    className={`h-full bg-gradient-to-r ${getHDCColor(healthData.protocols.hdc.efficiency)} transition-all duration-500 ease-out`}
                    style={{ width: `${hdcPercentage}%` }}
                  ></div>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-sm font-bold text-white drop-shadow-lg">
                      {healthData.protocols.hdc.efficiency}%
                    </span>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-3 gap-2 text-center text-xs">
                <div className="bg-gray-700/50 rounded p-2">
                  <div className="text-gray-400">MIN</div>
                  <div className="font-bold">12%</div>
                </div>
                <div className="bg-umaja-blue/20 rounded p-2 border border-umaja-blue/50">
                  <div className="text-gray-400">AKTUELL</div>
                  <div className="font-bold text-umaja-blue">{healthData.protocols.hdc.efficiency}%</div>
                </div>
                <div className="bg-gray-700/50 rounded p-2">
                  <div className="text-gray-400">MAX</div>
                  <div className="font-bold">28%</div>
                </div>
              </div>
            </div>

            {/* Huququh Protocol Card */}
            <div className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700 hover:border-umaja-gold transition-colors">
              <div className="flex items-center gap-2 mb-4">
                <div className="w-3 h-3 bg-umaja-gold rounded-full"></div>
                <h2 className="text-xl font-semibold text-umaja-gold">Huqúqu'lláh Protocol</h2>
              </div>

              <div className="mb-4">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-sm text-gray-400">81/19 Allocation System</span>
                  <span className={`text-xs px-2 py-1 rounded ${
                    healthData.protocols.huququh.compliant 
                      ? 'bg-green-900/50 text-green-400 border border-green-500/50'
                      : 'bg-red-900/50 text-red-400 border border-red-500/50'
                  }`}>
                    {healthData.protocols.huququh.compliant ? '✓ COMPLIANT' : '✗ NON-COMPLIANT'}
                  </span>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                {/* Architect Card */}
                <div className="bg-gradient-to-br from-umaja-blue/20 to-umaja-blue/5 rounded-lg p-4 border border-umaja-blue/30">
                  <div className="text-xs text-gray-400 mb-1">ARCHITECT</div>
                  <div className="text-4xl font-bold text-umaja-blue mb-2">
                    {healthData.protocols.huququh.architect}
                  </div>
                  <div className="text-xs text-gray-500">
                    {healthData.protocols.huququh.architect}% der Allokation
                  </div>
                  
                  {/* Visual bar */}
                  <div className="mt-3 h-2 bg-gray-700 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-umaja-blue"
                      style={{ width: `${healthData.protocols.huququh.architect}%` }}
                    ></div>
                  </div>
                </div>

                {/* Justice Card */}
                <div className="bg-gradient-to-br from-umaja-gold/20 to-umaja-gold/5 rounded-lg p-4 border border-umaja-gold/30">
                  <div className="text-xs text-gray-400 mb-1">JUSTICE</div>
                  <div className="text-4xl font-bold text-umaja-gold mb-2">
                    {healthData.protocols.huququh.justice}
                  </div>
                  <div className="text-xs text-gray-500">
                    {healthData.protocols.huququh.justice}% der Allokation
                  </div>
                  
                  {/* Visual bar */}
                  <div className="mt-3 h-2 bg-gray-700 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-umaja-gold"
                      style={{ width: `${healthData.protocols.huququh.justice}%` }}
                    ></div>
                  </div>
                </div>
              </div>

              {/* Pie Chart Visualization */}
              <div className="mt-6 flex items-center justify-center">
                <div className="relative w-32 h-32">
                  <svg className="transform -rotate-90" viewBox="0 0 100 100">
                    {/* Justice slice (19%) */}
                    <circle
                      cx="50"
                      cy="50"
                      r="40"
                      fill="none"
                      stroke="#d4af37"
                      strokeWidth="20"
                      strokeDasharray={`${healthData.protocols.huququh.justice * 2.51} ${(100 - healthData.protocols.huququh.justice) * 2.51}`}
                    />
                    {/* Architect slice (81%) */}
                    <circle
                      cx="50"
                      cy="50"
                      r="40"
                      fill="none"
                      stroke="#1e40af"
                      strokeWidth="20"
                      strokeDasharray={`${healthData.protocols.huququh.architect * 2.51} ${(100 - healthData.protocols.huququh.architect) * 2.51}`}
                      strokeDashoffset={`-${healthData.protocols.huququh.justice * 2.51}`}
                    />
                  </svg>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <div className="text-center">
                      <div className="text-xs text-gray-400">SPLIT</div>
                      <div className="text-sm font-bold">81/19</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <footer className="mt-8 text-center text-gray-500 text-sm">
          <p>UMAJA OMEGA CORE Dashboard • Real-time Protocol Monitoring</p>
          <p className="mt-1">Polling Interval: 2s • Backend: http://localhost:8080</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
