

%% Calculation of one-third octave band frequency vector
fmstart=0.9765625;
fmend=16000;
B=1/3;

Baender = 1/B * log2(fmend/fmstart)+1;
i = 1:Baender;
freq_T = fmstart*2.^((i-1)*B);  % axis x

%% additional input data
subs=1;

   %% caculation of Modes in Band
    function obj = ModenProTerzBand(para,freq_T)
        
        f_o=freq_T*2^(B/2);
        f_u=freq_T*2^(-B/2);
        
        Delta_F=zeros(subs,length(freq_T));
        
        for i=1:subs
           Delta_F(i,:)=f_o-f_u; 
        end
        
        ModDichteOben=ModaleDichte(para,f_o);
        ModDichteUnten=ModaleDichte(para,f_u);
        
        %effective bending
        obj.bending=0.5*(ModDichteOben.bending+ModDichteUnten.bending).*Delta_F*2*pi;
        %shear
        obj.shear=0.5*(ModDichteOben.shear+ModDichteUnten.shear).*Delta_F*2*pi;
        %longitudinal
        obj.compressional=0.5*(ModDichteOben.compressional+ModDichteUnten.compressional).*Delta_F*2*pi;
        
        obj.sum=obj.bending+obj.shear+obj.compressional;
        
        obj.freq=freq_T;
        obj.para=para;
        
    end

  