// Variáveis globais
let currentPage = 'store';
let isVideoPlaying = false;
let rainActive = false;

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    setupThumbnailGallery();
});

// Event Listeners
function initializeEventListeners() {
    // Botão de compra
    const buyNowBtn = document.getElementById('buy-now-btn');
    if (buyNowBtn) {
        buyNowBtn.addEventListener('click', showPurchasePage);
    }

    // Botão voltar da página de compra
    const backToStoreBtn = document.getElementById('back-to-store');
    if (backToStoreBtn) {
        backToStoreBtn.addEventListener('click', showStorePage);
    }

    // Botão confirmar compra
    const confirmPurchaseBtn = document.getElementById('confirm-purchase-btn');
    if (confirmPurchaseBtn) {
        confirmPurchaseBtn.addEventListener('click', processPurchase);
    }

    // Botão jogar agora
    const playNowBtn = document.getElementById('play-now-btn');
    if (playNowBtn) {
        playNowBtn.addEventListener('click', launchGame);
    }

    // Botão secreto
    const secretBtn = document.getElementById('secret-btn');
    if (secretBtn) {
        secretBtn.addEventListener('click', showTributeVideo);
    }

    // Botão fechar vídeo
    const closeVideoBtn = document.getElementById('close-video');
    if (closeVideoBtn) {
        closeVideoBtn.addEventListener('click', closeTributeVideo);
    }

    // Clique fora do vídeo para fechar
    const videoPlayer = document.getElementById('video-player');
    if (videoPlayer) {
        videoPlayer.addEventListener('click', function(e) {
            if (e.target === videoPlayer) {
                closeTributeVideo();
            }
        });
    }

    // Tecla ESC para fechar vídeo
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && isVideoPlaying) {
            closeTributeVideo();
        }
    });
}

// Galeria de thumbnails
function setupThumbnailGallery() {
    const thumbnails = document.querySelectorAll('.thumbnail');
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            changeMainImage(this.src);
            
            // Atualizar thumbnail ativo
            thumbnails.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Trocar imagem principal
function changeMainImage(src) {
    const mainImage = document.getElementById('main-game-image');
    if (mainImage) {
        // Efeito de fade
        mainImage.style.opacity = '0';
        setTimeout(() => {
            mainImage.src = src;
            mainImage.style.opacity = '1';
        }, 200);
    }
}

// Mostrar página de compra
function showPurchasePage() {
    const storePage = document.querySelector('.main-content');
    const purchasePage = document.getElementById('purchase-page');
    
    if (storePage && purchasePage) {
        // Animação de saída da loja
        storePage.style.transform = 'translateX(-100%)';
        storePage.style.opacity = '0';
        
        setTimeout(() => {
            storePage.style.display = 'none';
            purchasePage.classList.remove('hidden');
            
            // Animação de entrada da página de compra
            purchasePage.style.transform = 'translateX(100%)';
            purchasePage.style.opacity = '0';
            
            setTimeout(() => {
                purchasePage.style.transform = 'translateX(0)';
                purchasePage.style.opacity = '1';
                purchasePage.style.transition = 'all 0.5s ease';
            }, 50);
        }, 300);
    }
    
    currentPage = 'purchase';
}

// Mostrar página da loja
function showStorePage() {
    const storePage = document.querySelector('.main-content');
    const purchasePage = document.getElementById('purchase-page');
    
    if (storePage && purchasePage) {
        // Animação de saída da página de compra
        purchasePage.style.transform = 'translateX(100%)';
        purchasePage.style.opacity = '0';
        
        setTimeout(() => {
            purchasePage.classList.add('hidden');
            storePage.style.display = 'block';
            
            // Resetar estilos da loja
            storePage.style.transform = 'translateX(0)';
            storePage.style.opacity = '1';
            storePage.style.transition = 'all 0.5s ease';
        }, 300);
    }
    
    currentPage = 'store';
}

// Processar compra
function processPurchase() {
    const loadingScreen = document.getElementById('loading-screen');
    const purchasePage = document.getElementById('purchase-page');
    
    if (loadingScreen && purchasePage) {
        // Mostrar tela de carregamento
        loadingScreen.classList.remove('hidden');
        
        // Simular progresso de carregamento
        simulateLoading(() => {
            // Esconder tela de carregamento e página de compra
            loadingScreen.classList.add('hidden');
            purchasePage.classList.add('hidden');
            
            // Mostrar página de sucesso
            showSuccessPage();
        });
    }
}

// Simular carregamento
function simulateLoading(callback) {
    const progressBar = document.getElementById('loading-progress');
    let progress = 0;
    
    const interval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress > 100) progress = 100;
        
        if (progressBar) {
            progressBar.style.width = progress + '%';
        }
        
        if (progress >= 100) {
            clearInterval(interval);
            setTimeout(callback, 500);
        }
    }, 200);
}

// Mostrar página de sucesso
function showSuccessPage() {
    const successPage = document.getElementById('success-page');
    
    if (successPage) {
        successPage.classList.remove('hidden');
        
        // Animação de entrada
        successPage.style.opacity = '0';
        successPage.style.transform = 'scale(0.9)';
        
        setTimeout(() => {
            successPage.style.opacity = '1';
            successPage.style.transform = 'scale(1)';
            successPage.style.transition = 'all 0.5s ease';
        }, 50);
    }
    
    currentPage = 'success';
}

// Lançar jogo
function launchGame() {
    // Mostrar tela de carregamento novamente
    const loadingScreen = document.getElementById('loading-screen');
    const successPage = document.getElementById('success-page');
    
    if (loadingScreen && successPage) {
        successPage.classList.add('hidden');
        loadingScreen.classList.remove('hidden');
        
        // Atualizar texto de carregamento
        const loadingContent = loadingScreen.querySelector('.loading-content h2');
        const loadingText = loadingScreen.querySelector('.loading-content p');
        
        if (loadingContent) loadingContent.textContent = 'Iniciando Sinuca Delícia...';
        if (loadingText) loadingText.textContent = 'Preparando a mesa de bilhar para você.';
        
        // Simular carregamento do jogo
        simulateLoading(() => {
            loadingScreen.classList.add('hidden');
            
            // Tentar executar o jogo Python
            executeGame();
        });
    }
}

// Executar jogo
function executeGame() {
    try {
        // Detectar sistema operacional
        const isWindows = navigator.platform.indexOf('Win') > -1;
        const isMac = navigator.platform.indexOf('Mac') > -1;
        const isLinux = navigator.platform.indexOf('Linux') > -1;
        
        // Mostrar mensagem de que o jogo está sendo executado
        showGameLaunchMessage(isWindows, isMac, isLinux);
        
        // Tentar diferentes métodos de execução baseado no sistema
        if (isWindows) {
            // Para Windows, tentar executar o arquivo .bat
            tryExecuteWindows();
        } else if (isLinux || isMac) {
            // Para Linux/Mac, tentar executar o script shell
            tryExecuteUnix();
        } else {
            // Sistema não identificado, mostrar instruções manuais
            showManualInstructions();
        }
        
    } catch (error) {
        console.error('Erro ao executar o jogo:', error);
        showGameLaunchError();
    }
}

// Tentar executar no Windows
function tryExecuteWindows() {
    try {
        // Tentar abrir o arquivo .bat
        const link = document.createElement('a');
        link.href = 'executar_jogo.bat';
        link.download = 'executar_jogo.bat';
        link.click();
        
        setTimeout(() => {
            showWindowsInstructions();
        }, 2000);
    } catch (error) {
        showManualInstructions();
    }
}

// Tentar executar no Unix (Linux/Mac)
function tryExecuteUnix() {
    try {
        // Tentar abrir o script shell
        const link = document.createElement('a');
        link.href = 'executar_jogo.sh';
        link.download = 'executar_jogo.sh';
        link.click();
        
        setTimeout(() => {
            showUnixInstructions();
        }, 2000);
    } catch (error) {
        showManualInstructions();
    }
}

// Mostrar mensagem de lançamento do jogo
function showGameLaunchMessage(isWindows, isMac, isLinux) {
    // Criar overlay de mensagem
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: 'Motiva Sans', sans-serif;
    `;
    
    let systemMessage = '';
    if (isWindows) {
        systemMessage = 'O arquivo executar_jogo.bat será baixado. Execute-o para iniciar o jogo.';
    } else if (isLinux || isMac) {
        systemMessage = 'O arquivo executar_jogo.sh será baixado. Execute-o no terminal para iniciar o jogo.';
    } else {
        systemMessage = 'Execute o arquivo "em movimento sinuca.py" na pasta do jogo usando Python.';
    }
    
    overlay.innerHTML = `
        <div style="text-align: center; max-width: 600px; padding: 40px;">
            <div style="font-size: 60px; margin-bottom: 20px;">🎮</div>
            <h2 style="color: #66c0f4; font-size: 28px; margin-bottom: 15px;">Preparando Sinuca Delícia!</h2>
            <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
                ${systemMessage}
            </p>
            <p style="font-size: 14px; color: #8f98a0; margin-bottom: 20px;">
                Certifique-se de que o Python e pygame estão instalados no seu sistema.
            </p>
            <button onclick="this.parentElement.parentElement.remove()" 
                    style="background: linear-gradient(45deg, #5c7e10, #beee11); 
                           color: #1b2838; border: none; padding: 15px 25px; 
                           border-radius: 6px; font-weight: 600; cursor: pointer; 
                           font-size: 16px;">
                Entendi
            </button>
        </div>
    `;
    
    document.body.appendChild(overlay);
}

// Mostrar instruções para Windows
function showWindowsInstructions() {
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 10001;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: 'Motiva Sans', sans-serif;
    `;
    
    overlay.innerHTML = `
        <div style="text-align: center; max-width: 700px; padding: 40px;">
            <div style="font-size: 50px; margin-bottom: 20px;">🪟</div>
            <h2 style="color: #66c0f4; font-size: 24px; margin-bottom: 15px;">Instruções para Windows</h2>
            <div style="text-align: left; background: rgba(42, 71, 94, 0.3); padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <p style="margin-bottom: 10px;"><strong>1.</strong> Localize o arquivo "executar_jogo.bat" baixado</p>
                <p style="margin-bottom: 10px;"><strong>2.</strong> Clique duas vezes no arquivo para executar</p>
                <p style="margin-bottom: 10px;"><strong>3.</strong> Se aparecer um aviso de segurança, clique em "Executar mesmo assim"</p>
                <p style="margin-bottom: 10px;"><strong>4.</strong> O jogo será iniciado automaticamente</p>
            </div>
            <p style="font-size: 14px; color: #8f98a0; margin-bottom: 20px;">
                Se o Python não estiver instalado, baixe em: <span style="color: #66c0f4;">python.org</span>
            </p>
            <button onclick="this.parentElement.parentElement.remove()" 
                    style="background: linear-gradient(45deg, #5c7e10, #beee11); 
                           color: #1b2838; border: none; padding: 15px 25px; 
                           border-radius: 6px; font-weight: 600; cursor: pointer; 
                           font-size: 16px;">
                Entendi
            </button>
        </div>
    `;
    
    document.body.appendChild(overlay);
}

// Mostrar instruções para Unix (Linux/Mac)
function showUnixInstructions() {
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 10001;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: 'Motiva Sans', sans-serif;
    `;
    
    overlay.innerHTML = `
        <div style="text-align: center; max-width: 700px; padding: 40px;">
            <div style="font-size: 50px; margin-bottom: 20px;">🐧</div>
            <h2 style="color: #66c0f4; font-size: 24px; margin-bottom: 15px;">Instruções para Linux/Mac</h2>
            <div style="text-align: left; background: rgba(42, 71, 94, 0.3); padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <p style="margin-bottom: 10px;"><strong>1.</strong> Abra o terminal</p>
                <p style="margin-bottom: 10px;"><strong>2.</strong> Navegue até a pasta onde baixou o arquivo</p>
                <p style="margin-bottom: 10px;"><strong>3.</strong> Execute: <code style="background: #1b2838; padding: 2px 6px; border-radius: 3px;">chmod +x executar_jogo.sh</code></p>
                <p style="margin-bottom: 10px;"><strong>4.</strong> Execute: <code style="background: #1b2838; padding: 2px 6px; border-radius: 3px;">./executar_jogo.sh</code></p>
            </div>
            <p style="font-size: 14px; color: #8f98a0; margin-bottom: 20px;">
                Certifique-se de ter Python3 e pygame instalados
            </p>
            <button onclick="this.parentElement.parentElement.remove()" 
                    style="background: linear-gradient(45deg, #5c7e10, #beee11); 
                           color: #1b2838; border: none; padding: 15px 25px; 
                           border-radius: 6px; font-weight: 600; cursor: pointer; 
                           font-size: 16px;">
                Entendi
            </button>
        </div>
    `;
    
    document.body.appendChild(overlay);
}

// Mostrar instruções manuais
function showManualInstructions() {
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 10001;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-family: 'Motiva Sans', sans-serif;
    `;
    
    overlay.innerHTML = `
        <div style="text-align: center; max-width: 700px; padding: 40px;">
            <div style="font-size: 50px; margin-bottom: 20px;">⚙️</div>
            <h2 style="color: #66c0f4; font-size: 24px; margin-bottom: 15px;">Execução Manual</h2>
            <div style="text-align: left; background: rgba(42, 71, 94, 0.3); padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                <p style="margin-bottom: 10px;"><strong>1.</strong> Certifique-se de ter Python instalado</p>
                <p style="margin-bottom: 10px;"><strong>2.</strong> Instale pygame: <code style="background: #1b2838; padding: 2px 6px; border-radius: 3px;">pip install pygame</code></p>
                <p style="margin-bottom: 10px;"><strong>3.</strong> Navegue até a pasta "jogo"</p>
                <p style="margin-bottom: 10px;"><strong>4.</strong> Execute: <code style="background: #1b2838; padding: 2px 6px; border-radius: 3px;">python "em movimento sinuca.py"</code></p>
            </div>
            <p style="font-size: 14px; color: #8f98a0; margin-bottom: 20px;">
                O jogo está localizado na pasta "jogo" do site
            </p>
            <button onclick="this.parentElement.parentElement.remove()" 
                    style="background: linear-gradient(45deg, #5c7e10, #beee11); 
                           color: #1b2838; border: none; padding: 15px 25px; 
                           border-radius: 6px; font-weight: 600; cursor: pointer; 
                           font-size: 16px;">
                Entendi
            </button>
        </div>
    `;
    
    document.body.appendChild(overlay);
}

// Mostrar erro de lançamento do jogo
function showGameLaunchError() {
    alert('Erro ao executar o jogo. Verifique se o Python está instalado e tente executar o arquivo manualmente.');
}

// Mostrar vídeo tributo
function showTributeVideo() {
    const videoPlayer = document.getElementById('video-player');
    const rainOverlay = document.getElementById('rain-overlay');
    const video = document.getElementById('tribute-video');
    
    if (videoPlayer && rainOverlay && video) {
        // Mostrar overlay de chuva
        rainOverlay.classList.remove('hidden');
        rainActive = true;
        
        // Mostrar player de vídeo
        setTimeout(() => {
            videoPlayer.classList.remove('hidden');
            isVideoPlaying = true;
            
            // Reproduzir vídeo
            video.play().catch(e => {
                console.log('Erro ao reproduzir vídeo:', e);
            });
            
            // Adicionar efeito de fade suave
            videoPlayer.style.opacity = '0';
            setTimeout(() => {
                videoPlayer.style.opacity = '1';
                videoPlayer.style.transition = 'opacity 0.5s ease';
            }, 100);
            
        }, 500);
    }
}

// Fechar vídeo tributo
function closeTributeVideo() {
    const videoPlayer = document.getElementById('video-player');
    const rainOverlay = document.getElementById('rain-overlay');
    const video = document.getElementById('tribute-video');
    
    if (videoPlayer && rainOverlay && video) {
        // Pausar vídeo
        video.pause();
        video.currentTime = 0;
        
        // Fade out do player
        videoPlayer.style.opacity = '0';
        
        setTimeout(() => {
            videoPlayer.classList.add('hidden');
            isVideoPlaying = false;
            
            // Fade out da chuva
            rainOverlay.style.opacity = '0';
            
            setTimeout(() => {
                rainOverlay.classList.add('hidden');
                rainOverlay.style.opacity = '1'; // Reset para próxima vez
                rainActive = false;
            }, 500);
            
        }, 300);
    }
}

// Efeitos de hover nos botões
document.addEventListener('DOMContentLoaded', function() {
    // Adicionar efeitos sonoros visuais aos botões
    const buttons = document.querySelectorAll('button, .nav-link');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Efeito de partículas no hover do botão principal
    const buyButton = document.getElementById('buy-now-btn');
    if (buyButton) {
        buyButton.addEventListener('mouseenter', createParticleEffect);
    }
});

// Criar efeito de partículas
function createParticleEffect(event) {
    const button = event.target;
    const rect = button.getBoundingClientRect();
    
    for (let i = 0; i < 5; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            width: 4px;
            height: 4px;
            background: #beee11;
            border-radius: 50%;
            pointer-events: none;
            z-index: 1000;
            left: ${rect.left + Math.random() * rect.width}px;
            top: ${rect.top + Math.random() * rect.height}px;
            animation: particle-float 1s ease-out forwards;
        `;
        
        document.body.appendChild(particle);
        
        setTimeout(() => {
            particle.remove();
        }, 1000);
    }
}

// Adicionar CSS para animação de partículas
const style = document.createElement('style');
style.textContent = `
    @keyframes particle-float {
        0% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
        100% {
            opacity: 0;
            transform: translateY(-50px) scale(0);
        }
    }
`;
document.head.appendChild(style);

// Função para detectar se é mobile
function isMobile() {
    return window.innerWidth <= 768;
}

// Ajustar layout para mobile
function adjustForMobile() {
    if (isMobile()) {
        // Ajustes específicos para mobile
        const gameContent = document.querySelector('.game-content');
        if (gameContent) {
            gameContent.style.gridTemplateColumns = '1fr';
        }
    }
}

// Executar ajustes no redimensionamento
window.addEventListener('resize', adjustForMobile);

// Animação de entrada da página
document.addEventListener('DOMContentLoaded', function() {
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            mainContent.style.opacity = '1';
            mainContent.style.transform = 'translateY(0)';
            mainContent.style.transition = 'all 0.8s ease';
        }, 100);
    }
});

// Preload de imagens para melhor performance
function preloadImages() {
    const images = [
        'da4e9168-ee9e-4475-81a5-38f7b30c0425.png',
        'cd1f75c5-0c87-441a-9b68-72b87cfe1a38.png',
        'fd22294c-f629-4235-b900-4275107baab9.png',
        '3d5130ec-1c2c-41c2-b67c-a26835070b49.png'
    ];
    
    images.forEach(src => {
        const img = new Image();
        img.src = src;
    });
}

// Executar preload
document.addEventListener('DOMContentLoaded', preloadImages);

// Adicionar efeito de scroll suave
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll para links internos
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Função para salvar progresso (localStorage)
function saveProgress(data) {
    try {
        localStorage.setItem('sinuca-delicia-progress', JSON.stringify(data));
    } catch (e) {
        console.log('Erro ao salvar progresso:', e);
    }
}

// Função para carregar progresso
function loadProgress() {
    try {
        const data = localStorage.getItem('sinuca-delicia-progress');
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.log('Erro ao carregar progresso:', e);
        return null;
    }
}

// Salvar quando o jogo é "comprado"
function markGameAsPurchased() {
    saveProgress({
        purchased: true,
        purchaseDate: new Date().toISOString(),
        timesPlayed: 0
    });
}

// Verificar se o jogo já foi comprado
function checkIfGamePurchased() {
    const progress = loadProgress();
    return progress && progress.purchased;
}

// Atualizar interface baseado no status de compra
document.addEventListener('DOMContentLoaded', function() {
    if (checkIfGamePurchased()) {
        const buyButton = document.getElementById('buy-now-btn');
        if (buyButton) {
            buyButton.innerHTML = '<span class="btn-icon">▶️</span>JOGAR AGORA';
            buyButton.onclick = launchGame;
        }
    }
});

console.log('🎮 Sinuca Delícia - Site carregado com sucesso!');

