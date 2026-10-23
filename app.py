```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NAN Agenda Automática | Sistemas VIP para Nail Artists</title>
  <!-- Google Fonts: Cinzel & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            cinzel: ['"Cinzel"', 'serif'],
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          },
          colors: {
            gold: {
              100: '#FFFBEA',
              200: '#FDEEAA',
              300: '#FBDC6D',
              400: '#F5C438',
              500: '#D4AF37', /* Oro pulido clásico */
              600: '#B8860B',
              700: '#8C6709',
              800: '#5F4506',
              900: '#322303',
            },
            noir: {
              950: '#070707',
              900: '#0c0b0a',
              850: '#121110',
              800: '#171615',
              700: '#23211f',
            }
          },
          boxShadow: {
            'gold-glow': '0 0 35px -5px rgba(212, 175, 55, 0.35)',
            'gold-card': '0 12px 36px -8px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(212, 175, 55, 0.28)',
            'wa-glow': '0 0 30px rgba(34, 197, 94, 0.45)',
          }
        }
      }
    }
  </script>

  <style>
    /* Efecto metalizado oro realista */
    .gold-foil {
      background: linear-gradient(135deg, #FFF099 0%, #D4AF37 35%, #F5C438 50%, #AA771C 75%, #FDEEAA 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .gold-plate-badge {
      background: linear-gradient(145deg, #FFF4A3 0%, #E3BC42 22%, #C49A24 48%, #FFEB8A 72%, #8C6409 100%);
      box-shadow: 
        0 4px 18px rgba(0, 0, 0, 0.9),
        inset 0 1px 2px rgba(255, 255, 255, 0.9),
        inset 0 -1px 3px rgba(80, 52, 2, 0.9),
        0 0 25px rgba(212, 175, 55, 0.3);
      border: 1px solid #755208;
    }

    .gold-border-glow {
      position: relative;
      background: #141312;
      border: 1px solid rgba(212, 175, 55, 0.32);
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.7);
    }
    .gold-border-glow::before {
      content: '';
      position: absolute;
      inset: -1px;
      border-radius: inherit;
      padding: 1px;
      background: linear-gradient(135deg, rgba(253, 238, 170, 0.5) 0%, rgba(212, 175, 55, 0.1) 40%, rgba(140, 103, 9, 0.4) 100%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
    }

    /* Animación pulso sutil del botón WhatsApp */
    @keyframes subtlePulse {
      0%, 100% {
        transform: scale(1);
        box-shadow: 0 0 28px rgba(34, 197, 94, 0.5);
      }
      50% {
        transform: scale(1.02);
        box-shadow: 0 0 45px rgba(34, 197, 94, 0.75);
      }
    }
    .wa-pulse {
      animation: subtlePulse 3s infinite ease-in-out;
    }

    /* Patrón de fondo estilo textura seda oscura */
    .bg-damask {
      background-color: #080808;
      background-image: radial-gradient(circle at 50% 0%, rgba(35, 30, 20, 0.5) 0%, rgba(8, 8, 8, 1) 75%);
    }

    /* Scrollbar oculta pero funcional */
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
</head>

<body class="bg-damask min-h-screen text-stone-200 font-sans flex items-center justify-center p-2 sm:p-6 antialiased selection:bg-gold-500 selection:text-black">

  <!-- ================= DISPOSITIVO MÓVIL ESTILO IPHONE FRAME ================= -->
  <main class="w-full max-w-[430px] bg-noir-950 rounded-[44px] border-[2px] border-stone-800/80 shadow-[0_25px_80px_rgba(0,0,0,0.95)] overflow-hidden relative pb-8 my-auto">
    
    <!-- Barra superior simulada (Notch y sensor) -->
    <div class="pt-3 pb-2 flex justify-center items-center relative z-20">
      <div class="w-28 h-4 bg-stone-900 rounded-full border border-stone-800 flex items-center justify-end px-3">
        <span class="w-2 h-2 rounded-full bg-stone-950 block border border-stone-800"></span>
      </div>
    </div>

    <!-- Contenido Scrollable -->
    <div class="px-5 pt-3 pb-6 flex flex-col items-center">
      
      <!-- 1. PLACA EMBLEMÁTICA DE ULTRA LUJO 'NAN' -->
      <div class="mt-2 mb-4 relative">
        <div class="gold-plate-badge w-36 h-20 rounded-md p-1 flex items-center justify-center relative cursor-pointer transform hover:scale-105 transition-transform duration-300">
          <!-- Borde interno biselado de joyería -->
          <div class="w-full h-full border border-[#6b4c05] rounded-sm flex items-center justify-center bg-gradient-to-b from-[#ffea8a] via-[#e2ba3f] to-[#be8e1a]">
            <span class="font-cinzel text-black text-3xl font-extrabold tracking-[0.22em] pl-1 drop-shadow-[0_1px_1px_rgba(255,255,255,0.7)]">
              NAN
            </span>
          </div>
        </div>
      </div>

      <!-- 2. SUBTÍTULO DORADO CON ESPACIADO ELEGANTE -->
      <h2 class="font-cinzel text-center text-xs tracking-[0.38em] text-[#d4af37] font-bold uppercase mb-6 drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
        AGENDA AUTOMÁTICA
      </h2>

      <!-- 3. TARJETA CENTRAL HERO (Copia idéntica y refinada) -->
      <div class="w-full gold-border-glow rounded-3xl p-5 mb-6">
        <div class="flex items-center gap-4">
          <!-- Ícono de Calendario con destellos dorados en SVG de alta precisión -->
          <div class="flex-shrink-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-[#282216] to-[#12110e] border border-gold-500/30 flex items-center justify-center shadow-inner">
            <svg class="w-10 h-10 text-gold-400 drop-shadow-[0_0_8px_rgba(245,196,56,0.6)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
              <circle cx="8" cy="14" r="0.8" fill="currentColor"></circle>
              <circle cx="12" cy="14" r="0.8" fill="currentColor"></circle>
              <circle cx="16" cy="14" r="0.8" fill="currentColor"></circle>
              <circle cx="8" cy="18" r="0.8" fill="currentColor"></circle>
              <circle cx="12" cy="18" r="0.8" fill="currentColor"></circle>
              <!-- Destello de estrella ✨ -->
              <path d="M19 3v4M21 5h-4" stroke="#FFF4A3" stroke-width="1.8" />
            </svg>
          </div>

          <!-- Texto descriptivo potente -->
          <div class="flex-1">
            <p class="text-white text-[15px] font-bold leading-snug tracking-tight">
              Para que agende sola y le caigan clientas a su <span class="gold-foil font-extrabold">WhatsApp 24/7</span>
            </p>
          </div>
        </div>
      </div>

      <!-- 4. LISTA DE BENEFICIOS CON ÍCONOS DORADOS CIRCULARES -->
      <div class="w-full space-y-4 px-1 mb-6">
        <!-- Beneficio 1 -->
        <div class="flex items-center gap-3.5 group">
          <div class="w-8 h-8 rounded-full border border-gold-500/50 flex items-center justify-center bg-noir-850 shadow-sm flex-shrink-0 group-hover:border-gold-400 transition-colors">
            <svg class="w-4 h-4 text-gold-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <span class="text-stone-300 text-[13.5px] font-medium tracking-wide">
            Responde al instante a tus clientas
          </span>
        </div>

        <!-- Beneficio 2 -->
        <div class="flex items-center gap-3.5 group">
          <div class="w-8 h-8 rounded-full border border-gold-500/50 flex items-center justify-center bg-noir-850 shadow-sm flex-shrink-0 group-hover:border-gold-400 transition-colors">
            <svg class="w-4 h-4 text-gold-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="4" width="18" height="18" rx="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
              <path d="M8 14h.01M12 14h.01M16 14h.01M8 17h.01M12 17h.01"></path>
            </svg>
          </div>
          <span class="text-stone-300 text-[13.5px] font-medium tracking-wide">
            Confirma y recuerda citas automáticamente
          </span>
        </div>

        <!-- Beneficio 3 -->
        <div class="flex items-center gap-3.5 group">
          <div class="w-8 h-8 rounded-full border border-gold-500/50 flex items-center justify-center bg-noir-850 shadow-sm flex-shrink-0 group-hover:border-gold-400 transition-colors">
            <svg class="w-4 h-4 text-gold-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
          </div>
          <span class="text-stone-300 text-[13.5px] font-medium tracking-wide">
            Capta más clientas desde Instagram y WhatsApp
          </span>
        </div>
      </div>

      <!-- 5. FILIGRANA ORNAMENTAL VINTAGE DORADA -->
      <div class="w-full flex items-center justify-center my-2 opacity-80">
        <svg class="w-44 h-5 text-gold-500" viewBox="0 0 200 20" fill="currentColor">
          <path d="M100 10 L108 5 L116 10 L108 15 Z" fill="#D4AF37"/>
          <path d="M100 10 L92 5 L84 10 L92 15 Z" fill="#D4AF37"/>
          <circle cx="100" cy="10" r="2.5" fill="#FFF4A3"/>
          <line x1="15" y1="10" x2="80" y2="10" stroke="#D4AF37" stroke-width="1" stroke-linecap="round"/>
          <line x1="120" y1="10" x2="185" y2="10" stroke="#D4AF37" stroke-width="1" stroke-linecap="round"/>
          <circle cx="15" cy="10" r="1.5" fill="#D4AF37"/>
          <circle cx="185" cy="10" r="1.5" fill="#D4AF37"/>
        </svg>
      </div>

      <!-- 6. TARJETA DE OFERTA EXCLUSIVA: $499 MXN -->
      <div class="w-full bg-gradient-to-b from-stone-900/90 to-noir-900 border border-gold-500/25 rounded-2xl p-4 my-3 text-center">
        <div class="inline-block bg-gold-500/10 border border-gold-500/40 text-gold-300 text-[10px] tracking-widest font-extrabold px-3 py-1 rounded-full uppercase mb-2">
          ⚡ Entrega en menos de 24 horas
        </div>
        <div class="text-xs text-stone-400 font-medium tracking-wide">
          Inversión total por tu link personalizado:
        </div>
        <div class="text-2xl font-black text-white mt-1">
          <span class="gold-foil text-3xl font-extrabold">$499 MXN</span>
        </div>
        <div class="text-[11px] text-stone-400 font-semibold italic mt-0.5">
          (Pago único • Sin mensualidades • Lista para usar)
        </div>
      </div>

      <!-- BOTÓN PARA ABRIR EL SIMULADOR INTERACTIVO (DEMO EN VIVO) -->
      <button onclick="toggleModal(true)" class="text-xs text-gold-400 font-bold uppercase tracking-widest underline decoration-gold-500/50 hover:text-gold-200 transition-colors mb-4 flex items-center gap-1.5 py-1">
        <span>✨ Ver cómo interactúa la clienta (Demo en vivo)</span>
      </button>

      <!-- 7. BOTÓN OFICIAL DE WHATSAPP (Verde Neón con Pulsación Suave) -->
      <a href="https://wa.me/5215539233647?text=¡Hola%20NAN%20Studio%20Tech!%20👋%20Quiero%20mi%20enlace%20personalizado%20de%20Agenda%20Automática%20por%20$499%20MXN%20para%20mi%20estudio%20de%20uñas."
         target="_blank" 
         class="w-full bg-[#22c55e] hover:bg-[#16a34a] text-white font-extrabold text-[15px] tracking-wide py-4 px-4 rounded-2xl flex items-center justify-center gap-2.5 shadow-wa-glow wa-pulse transition-all duration-300 mb-3 active:scale-95">
        <!-- Ícono oficial de WhatsApp SVG -->
        <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24">
          <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
        </svg>
        <span>Conectar mi WhatsApp</span>
      </a>

      <!-- 8. PIE DE PÁGINA ULTRA LIMPIO -->
      <div class="text-center space-y-1.5 mt-2">
        <p class="text-[11px] text-[#caa758] tracking-wider font-semibold">
          Sin complicaciones • Configuración total • Lista para tu Bio
        </p>
        <p class="text-[10px] text-stone-500 tracking-widest uppercase">
          NAN STUDIO TECH • Automatiza tu agenda de uñas
        </p>
      </div>

    </div>
  </main>

  <!-- ================= MODAL DE DEMO EN VIVO INTERACTIVA ================= -->
  <div id="demoModal" class="fixed inset-0 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4 z-50">
    <div class="bg-noir-900 border border-gold-500/40 rounded-3xl max-w-sm w-full p-6 text-stone-200 shadow-2xl relative">
      <!-- Botón cerrar -->
      <button onclick="toggleModal(false)" class="absolute top-4 right-4 text-stone-400 hover:text-white p-1 text-xl font-bold">
        ✕
      </button>

      <div class="text-center mb-4">
        <span class="text-xs text-gold-400 font-bold uppercase tracking-widest">Simulador en Tiempo Real</span>
        <h3 class="text-lg font-bold text-white mt-1">Cómo agenda tu clienta:</h3>
      </div>

      <div class="space-y-3.5 text-xs">
        <div>
          <label class="block text-stone-400 font-semibold mb-1">1. Elige el servicio:</label>
          <select id="simServicio" class="w-full bg-stone-950 border border-stone-700 rounded-xl p-2.5 text-stone-200 focus:border-gold-500 outline-none">
            <option value="Acrílico Escultural XL ($650 MXN - Anticipo: $200 MXN)">Acrílico Escultural XL ($650 MXN)</option>
            <option value="Soft Gel Express + Foil ($450 MXN - Anticipo: $150 MXN)">Soft Gel Express + Foil ($450 MXN)</option>
            <option value="Manicura Rusa + Nivelación ($400 MXN - Anticipo: $150 MXN)">Manicura Rusa + Nivelación ($400 MXN)</option>
          </select>
        </div>

        <div>
          <label class="block text-stone-400 font-semibold mb-1">2. Selecciona fecha y hora disponible:</label>
          <div class="grid grid-cols-2 gap-2">
            <input type="date" id="simFecha" class="w-full bg-stone-950 border border-stone-700 rounded-xl p-2 text-stone-200 text-xs focus:border-gold-500 outline-none">
            <select id="simHora" class="w-full bg-stone-950 border border-stone-700 rounded-xl p-2 text-stone-200 text-xs focus:border-gold-500 outline-none">
              <option>10:00 AM</option>
              <option>12:30 PM</option>
              <option>03:30 PM</option>
              <option>06:00 PM</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-stone-400 font-semibold mb-1">3. Nombre de la clienta:</label>
          <input type="text" id="simNombre" placeholder="Ej. Mariana Gómez" value="Mariana Gómez" class="w-full bg-stone-950 border border-stone-700 rounded-xl p-2.5 text-stone-200 focus:border-gold-500 outline-none">
        </div>

        <!-- Vista previa del mensaje que recibe la manicurista -->
        <div class="p-3 bg-stone-950/90 rounded-xl border border-gold-500/20 text-[11px] text-stone-300">
          <div class="font-bold text-gold-400 mb-1 flex items-center gap-1">
            <span>📲 Mensaje que te llegará listo:</span>
          </div>
          <p id="previewText" class="italic text-stone-400 leading-relaxed">
            "Hola! Deseo agendar Acrílico Escultural para el día seleccionado. Ya tengo listo mi anticipo, ¿me pasas tu tarjeta?"
          </p>
        </div>

        <button onclick="copiarSimulacion()" class="w-full bg-gold-500 hover:bg-gold-400 text-black font-bold py-3 rounded-xl uppercase tracking-wider text-xs transition-colors">
          Probar Enviar este Ejemplo
        </button>
      </div>
    </div>
  </div>

  <!-- SCRIPT INTERACTIVO -->
  <script>
    // Establecer fecha de mañana por defecto
    const today = new Date();
    today.setDate(today.getDate() + 1);
    document.getElementById('simFecha').value = today.toISOString().split('T')[0];

    function toggleModal(show) {
      const modal = document.getElementById('demoModal');
      if (show) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      } else {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    function copiarSimulacion() {
      const srv = document.getElementById('simServicio').value;
      const fch = document.getElementById('simFecha').value;
      const hr = document.getElementById('simHora').value;
      const nom = document.getElementById('simNombre').value || 'Clienta';

      const texto = `Hola NAN Studio! Estuve probando el simulador y me encantó. Quiero mi propio link de citas para agendar así a mis clientas por $499 MXN.`;
      const url = `https://wa.me/5215539233647?text=${encodeURIComponent(texto)}`;
      window.open(url, '_blank');
    }
  </script>

</body>
</html>
```