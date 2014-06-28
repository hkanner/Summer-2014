from scipy.signal import butter, lfilter

def butter_anypass(lowcut,highcut,fs,butterType, order=5):
    nyq=0.5*fs
    if lowcut!=None:
        low=lowcut/nyq
    else: low=None
    if highcut!=None:
        high=highcut/nyq
    else: high=None
    if low==None:
        b,a=butter(order,[high],btype=butterType)
    elif high==None:
        b,a=butter(order,[low],btype=butterType)
    else: b,a=butter(order,[low,high],btype=butterType)
    return b,a

def butter_anypass_filter(data,lowcut,highcut,fs,butterType,order=5):
    b,a=butter_anypass(lowcut,highcut,fs,butterType=butterType,order=order)
    y=lfilter(b,a,data)
    return y

if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz

    fs=5000.0
    lowcut=500.0
    #highcut=1250.0
# Frequency response for butterworth filter of different orders
    plt.figure(1)
    plt.clf()
    for order in [1,6,20]:
        b,a=butter_anypass(lowcut,None,fs,'lowpass',order=order)
        w,h=freqz(b,a,worN=2000)
        plt.plot((fs*0.5/np.pi)*w,abs(h),label="order =%d" %order)
        
    plt.plot([0,0.5*fs],[np.sqrt(0.5),np.sqrt(0.5)],'--',label='sqrt(0.5)')
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')
    
# Butterworth filter of noisy signal
    T=0.05
    nsamples=T*fs
    t=np.linspace(0,T,nsamples,endpoint=False)
    a=0.02
    f0=600
# Create combined noise and actual signal
    x=0.1*np.sin(2*np.pi*1.2*np.sqrt(t))
    x+=0.01*np.cos(2*np.pi*312*t +0.1)
    x+=a*np.cos(2*np.pi*f0*t +0.11)
    x+=0.03*np.cos(2*np.pi*2000*t)
    plt.figure(2)
    plt.clf()
    plt.plot(t,x,label="Noisy Signal")
# Filtered Signal
    y=butter_anypass_filter(x,lowcut,None,fs,'lowpass',order=20)
    plt.plot(t,y,label="Filtered Signal(%g Hz)"% f0)
    plt.xlabel('Time(seconds)')
    #plt.hlines([-a, a],0,T,linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='best')
    
    plt.show()
        
