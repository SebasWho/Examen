function [norm_audio] = normalizar(audio)
maximo = max(abs(audio));
n = length(audio);
norm_audio = zeros(n,1);
    for i = 1:1:n
        norm_audio(i) = audio(i)/maximo;
    end
    
end