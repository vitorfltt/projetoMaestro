# MAESTRO FRAMEWORK

# Pré-requisitos do Windows
1. Ter o PowerShell instalado no Windows: normalmente vem instalado por padrão;

2. Ter o Android Studio instalado no Windows: siga este passo a passo para a instalação;

3. Ter a variável ANDROID_HOME configurada nas variáveis de ambiente: basta adicionar o caminho da pasta \Android\Sdk nas variáveis de ambiente.

   -- Segue um vídeo do canal qazando mostrando como fazer: https://www.youtube.com/watch?v=yuKlc-a5z5k
   
4. Para confirmar que a variável ANDROID_HOME está configurada corretamente, execute no PowerShell: adb --version

5. Ter o Java JDK instalado e a variável JAVA_HOME configurada nas variáveis de ambiente.

   -- Segue um tutorial de como fazer a instalação do Java JDK e configurar a variável JAVA_HOME: https://www.youtube.com/watch?v=gIFgBMZX6e8


# Passo a Passo:
1. Instalação do WSL2 (Windows Subsystem for Linux) no Windows:

    -- Para instalar o WSL no Windows basta abrir o PowerShell como administrador e executar o comando: wsl --install

    -- Após executar o comando acima é necessário reiniciar o computador.

    -- Após a instalação abra o terminal WSL. Na primeira vez que o terminal WSL for aberto será solicitada a criação de um usuário e senha de administrador para o Linux.

    -- Para atualizar o Ubuntu execute no terminal WSL: sudo apt update e sudo apt upgrade

2. Instalação do Java no WSL:

    -- A instalação do Java JDK no WSL é feita simplesmente executando o comando no terminal WSL: sudo apt install openjdk-11-jdk
   
3. Instalação do Maestro no WSL:
   
    -- Antes de instalar o Maestro no WSL é necessário ter o programa unzip instalado. Com o terminal aberto execute: sudo apt-get install unzip

    -- Com o unzip instalado podemos instalar o Maestro executando no terminal: curl -Ls "https://get.maestro.mobile.dev" | bash

    -- Também é necessário configurar o comando maestro para ser reconhecido pelo WSL. Basta executar o comando no terminal: export PATH="$PATH":"$HOME/.maestro/bin"

    -- Para confirmar que o Maestro está instalado e configurado corretamente no WSL, execute: maestro --version

4. Instalação do Android no WSL:

    -- Primeiramente precisamos criar uma pasta Android no WSL e navegar até ela: mkdir Android e cd Android

    -- Dentro da pasta Android devemos criar uma pasta cmdline-tools e navegar até ela: mkdir cmdline-tools e cd cmdline-tools

    -- Em seguida precisamos baixar as ferramentas de linha de comando do Android dentro da pasta Android/cmdline-tools: wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip

    -- Após o download é necessário descompactar o arquivo das ferramentas de linha de comando do Android na pasta Android/cmdline-tools: unzip commandlinetools-linux.zip

    -- Com o arquivo das ferramentas de linha descompactado na pasta Android/cmdline-tools devemos executar: mv cmdline-tools latest

    -- Ao fim a estrutura das pastas ficará Android/cmdline-tools/latest.

    -- Após a instalação das ferramentas de linha de comando do Android é necessário editar o arquivo bashrc (arquivo de configuração do terminal WSL) e adicionar algumas linhas para tornar os comandos do                Android acessíveis através do terminal WSL.

    -- Para abrir o arquivo em modo de edição, basta executar: nano ~/.bashrc

     -- No fim do arquivo bashrc devemos adicionar as linhas abaixo:
           -- export ANDROID_HOME=$HOME/Android
           -- export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin/:$PATH

     -- Em seguida é necessário recarregar as configurações do terminal: source ~/.bashrc

     -- Para confirmar que as ferramentas de linha de comando do Android estão funcionando corretamente, execute: sdkmanager --list

     -- Com as ferramentas de linha de comando do Android funcionando corretamente, precisamos instalar o Android SDK Platform-Tools executando: sdkmanager --install "platform-tools"

     -- É necessário abrir novamente o arquivo bashrc: nano ~/.bashrc

     -- E então adicionar a linha abaixo no fim do arquivo: export PATH=$PATH:$ANDROID_HOME/platform-tools/:$PATH

     -- E novamente recarregar as configurações do terminal: source ~/.bashrc

     -- Para checar que as ferramentas do Android estão funcionando corretamente no WSL é necessário fechar o terminal, abri-lo novamente e executar o comando: adb --version

     -- Se tudo estiver configurado corertamenta a versão do adb exibida no terminal WSL é a mesma exibida no terminal Windows.

5. Configuração do adb para usar emulador com WSL
     -- Para utilizar o Maestro precisamos fazer algumas configurações para tornar o emulador executado no Windows acessível pelo terminal WSL.

     -- Primeiramente é necessário executar o emulador no Windows e então abrir o PowerShell e executar os comandos abaixo para rodar o servidor adb no Windows: adb kill-server e adb -a -P 5037 nodaemon server

     -- Então precisamos exibir e tomar nota do endereço IPV4 do Windows: ipconfig(no terminal do windows).

     -- Pegar o endereço IPv4 Address

     -- Com o PowerShell e emulador abertos no Windows, devemos abrir o terminal WSL e rodar os comandos abaixo substituindo ENDEREÇO_IPV4_WINDOWS pelo endereço exibido no passo anterior:

             -- adb kill-server
   
             -- export ADB_SERVER_SOCKET=tcp:{WINDOWS_IPV4_ADDRESS}:5037
   
             -- adb devices

      -- Se tudo estiver configurado corretamente o emulador aberto no Windows é listado no WSL, então está tudo preparado para executar o Maestro.

# Executando os testes no Maestro

     -- Agora que tudo está configurado corretamente podemos executar um arquivo de testes no Maestro com o comando:
             -- maestro --host {WINDOWS_IPV4_ADDRESS} test flow.yaml

     -- Também podemos abrir o Maestro Studio executando:
             -- maestro --host {WINDOWS_IPV4_ADDRESS} studio

     -- Também é possível explorar o Maestro mesmo se não tivermos um arquivo de testes ou uma APK criados previamente, basta executar os exemplos fornecidos pelo próprio framework:
             -- maestro download-samples
             #baixa os exemplos do Maestro
             -- cd ./samples
             #Navega até a pasta 'samples'
             -- adb install sample.apk
             #Instala a apk de exemplo 'sample.apk' no dispositivo em execução
             -- maestro --host {WINDOWS_IPV4_ADDRESS} test android-flow.yaml
             #Exemplo: maestro --host 0.0.0.0 test android-flow.yaml
             #Executa os testes do arquivo 'android-flow' no dispositivo em execução


 




























 



