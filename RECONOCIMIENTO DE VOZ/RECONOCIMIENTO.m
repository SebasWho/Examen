
function varargout = RECONOCIMIENTO(varargin)

gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @RECONOCIMIENTO_OpeningFcn, ...
                   'gui_OutputFcn',  @RECONOCIMIENTO_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end

function RECONOCIMIENTO_OpeningFcn(hObject, eventdata, handles, varargin)

handles.output = hObject;

guidata(hObject, handles);

function varargout = RECONOCIMIENTO_OutputFcn(hObject, eventdata, handles) 

varargout{1} = handles.output;


% --- Executes on button press in GRABAR.
function GRABAR_Callback(hObject, eventdata, handles)
global Palabra Fs;
clc
Fs=11025;
tgrabado=2;

audio=audiorecorder(Fs, 24, 1);
recordblocking(audio, tgrabado);
Palabra = audio.getaudiodata();
b=[1 -0.95];
fil=filter(b,1,Palabra);
audiowrite('Audio.wav',fil,Fs); 

set(handles.AUDIO); % Establece los ejes de graficación
axes(handles.AUDIO);
plot(Palabra);grid on;
msgbox('SE HA GRABADO CORRECTAMENTE');


function REPRODUCIR_Callback(hObject, eventdata, handles)
[Palabra,Fs]=audioread('Audio.wav');
soundsc(Palabra,11025);


% --- Executes on button press in IDENTIFICAR.
function IDENTIFICAR_Callback(hObject, eventdata, handles)

Audio=audioread('Audio.wav');
norm_Audio=normalizar(Audio);
fft_Audio=abs((fft(norm_Audio)));

minimo_error= 50000;

Frase=' ';

directorio =  dir([pwd '\' '*.wav']); 
for k = 1:length(directorio)
    dic_nom = directorio(k).name; 
    error=0;
    audio_dic=0;
    norm_dic=0;
    fft_dic=0;
    if ~strcmp(dic_nom,'Audio.wav')
        audio_dic = audioread(dic_nom);
        norm_dic=normalizar(audio_dic);
        fft_dic=abs((fft(norm_dic)));

        set(handles.FFTBD); 
        axes(handles.FFTBD);
        plot(fft_dic);grid on;

        set(handles.axes4); 
        axes(handles.axes4);
        plot(fft_Audio);grid on;
        
        error = mean(abs(fft_dic - fft_Audio));
        
        if error < minimo_error
            minimo_error=error
            Frase=dic_nom;
        end    

    end    

end
set(handles.edit3, 'string', upper(Frase(1:end-4)));



function edit3_Callback(hObject, eventdata, handles)


function edit3_CreateFcn(hObject, eventdata, handles)


if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
    


% --- Executes on button press in AGREGAR.
function AGREGAR_Callback(hObject, eventdata, handles)

Fs=11025; %frecuencia de muestreo
tiempograb=2; %Tiempo de grabacion
leer=get(handles.Leer,'String');
usuario=audiorecorder(Fs, 24, 1); %función de grabacion
recordblocking(usuario, tiempograb)
z = usuario.getaudiodata()
sound(z,Fs);
b=[1 -0.95];
fil=filter(b,1,z);

audiowrite(strcat(leer,'.wav'),fil,Fs);
 
msgbox('SE HA GRABADO CORRECTAMENTE');
guidata(hObject, handles);

function Leer_Callback(hObject, eventdata, handles)


function Leer_CreateFcn(hObject, eventdata, handles)


if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Exit.
function Exit_Callback(hObject, eventdata, handles)

exit;
