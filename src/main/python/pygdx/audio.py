from __future__ import annotations
from overload import overload


 
from abc import abstractmethod, ABC
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
 
class Sound(ABC):
    """com.badlogic.gdx.audio.Sound"""
 
    @staticmethod
    def __wrap(java_value: __Sound) -> 'Sound':
        return Sound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sound):
        """
        Dynamic initializer for Sound.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def loop(self, ):
        """public abstract long com.badlogic.gdx.audio.Sound.loop()"""
        pass

    @abstractmethod
    def setLooping(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.audio.Sound.setLooping(long,boolean)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.dispose()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.resume()"""
        pass

    @abstractmethod
    def play(self, arg0: float, arg1: float, arg2: float):
        """public abstract long com.badlogic.gdx.audio.Sound.play(float,float,float)"""
        pass

    @abstractmethod
    def loop(self, arg0: float):
        """public abstract long com.badlogic.gdx.audio.Sound.loop(float)"""
        pass

    @abstractmethod
    def loop(self, arg0: float, arg1: float, arg2: float):
        """public abstract long com.badlogic.gdx.audio.Sound.loop(float,float,float)"""
        pass

    @abstractmethod
    def play(self, ):
        """public abstract long com.badlogic.gdx.audio.Sound.play()"""
        pass

    @abstractmethod
    def setPan(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setPan(long,float,float)"""
        pass

    @abstractmethod
    def resume(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.resume(long)"""
        pass

    @abstractmethod
    def play(self, arg0: float):
        """public abstract long com.badlogic.gdx.audio.Sound.play(float)"""
        pass

    @abstractmethod
    def stop(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.stop()"""
        pass

    @abstractmethod
    def stop(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.stop(long)"""
        pass

    @abstractmethod
    def pause(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.pause(long)"""
        pass

    @abstractmethod
    def setPitch(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setPitch(long,float)"""
        pass

    @abstractmethod
    def setVolume(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setVolume(long,float)"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.pause()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.audio.Sound
from abc import abstractmethod, ABC
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
 
class Sound(ABC):
    """com.badlogic.gdx.audio.Sound"""
 
    @staticmethod
    def __wrap(java_value: __Sound) -> 'Sound':
        return Sound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sound):
        """
        Dynamic initializer for Sound.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def loop(self, ):
        """public abstract long com.badlogic.gdx.audio.Sound.loop()"""
        pass

    @abstractmethod
    def setLooping(self, arg0: int, arg1: bool):
        """public abstract void com.badlogic.gdx.audio.Sound.setLooping(long,boolean)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.dispose()"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.resume()"""
        pass

    @abstractmethod
    def play(self, arg0: float, arg1: float, arg2: float):
        """public abstract long com.badlogic.gdx.audio.Sound.play(float,float,float)"""
        pass

    @abstractmethod
    def loop(self, arg0: float):
        """public abstract long com.badlogic.gdx.audio.Sound.loop(float)"""
        pass

    @abstractmethod
    def loop(self, arg0: float, arg1: float, arg2: float):
        """public abstract long com.badlogic.gdx.audio.Sound.loop(float,float,float)"""
        pass

    @abstractmethod
    def play(self, ):
        """public abstract long com.badlogic.gdx.audio.Sound.play()"""
        pass

    @abstractmethod
    def setPan(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setPan(long,float,float)"""
        pass

    @abstractmethod
    def resume(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.resume(long)"""
        pass

    @abstractmethod
    def play(self, arg0: float):
        """public abstract long com.badlogic.gdx.audio.Sound.play(float)"""
        pass

    @abstractmethod
    def stop(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.stop()"""
        pass

    @abstractmethod
    def stop(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.stop(long)"""
        pass

    @abstractmethod
    def pause(self, arg0: int):
        """public abstract void com.badlogic.gdx.audio.Sound.pause(long)"""
        pass

    @abstractmethod
    def setPitch(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setPitch(long,float)"""
        pass

    @abstractmethod
    def setVolume(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.audio.Sound.setVolume(long,float)"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.audio.Sound.pause()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.audio.Sound 
 
 
# CLASS: com.badlogic.gdx.audio.AudioRecorder
from abc import abstractmethod, ABC
import com.badlogic.gdx.audio.AudioRecorder as __AudioRecorder
__AudioRecorder = __AudioRecorder
from builtins import int
 
class AudioRecorder(ABC):
    """com.badlogic.gdx.audio.AudioRecorder"""
 
    @staticmethod
    def __wrap(java_value: __AudioRecorder) -> 'AudioRecorder':
        return AudioRecorder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AudioRecorder):
        """
        Dynamic initializer for AudioRecorder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.audio.AudioRecorder.dispose()"""
        pass

    @abstractmethod
    def read(self, arg0: 'short', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.audio.AudioRecorder.read(short[],int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.audio.Music$OnCompletionListener
from abc import abstractmethod, ABC
import com.badlogic.gdx.audio.Music as __Music_OnCompletionListener
__OnCompletionListener = __Music_OnCompletionListener.OnCompletionListener
 
class OnCompletionListener(ABC):
    """com.badlogic.gdx.audio.Music.OnCompletionListener"""
 
    @staticmethod
    def __wrap(java_value: __OnCompletionListener) -> 'OnCompletionListener':
        return OnCompletionListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OnCompletionListener):
        """
        Dynamic initializer for OnCompletionListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onCompletion(self, arg0: 'Music'):
        """public abstract void com.badlogic.gdx.audio.Music$OnCompletionListener.onCompletion(com.badlogic.gdx.audio.Music)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.audio.Music
from abc import abstractmethod, ABC
import com.badlogic.gdx.audio.Music as __Music
__Music = __Music
 
class Music(ABC):
    """com.badlogic.gdx.audio.Music"""
 
    @staticmethod
    def __wrap(java_value: __Music) -> 'Music':
        return Music(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Music):
        """
        Dynamic initializer for Music.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setLooping(self, arg0: bool):
        """public abstract void com.badlogic.gdx.audio.Music.setLooping(boolean)"""
        pass

    @abstractmethod
    def isPlaying(self, ):
        """public abstract boolean com.badlogic.gdx.audio.Music.isPlaying()"""
        pass

    @abstractmethod
    def play(self, ):
        """public abstract void com.badlogic.gdx.audio.Music.play()"""
        pass

    @abstractmethod
    def setPosition(self, arg0: float):
        """public abstract void com.badlogic.gdx.audio.Music.setPosition(float)"""
        pass

    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.audio.Music.pause()"""
        pass

    @abstractmethod
    def getPosition(self, ):
        """public abstract float com.badlogic.gdx.audio.Music.getPosition()"""
        pass

    @abstractmethod
    def isLooping(self, ):
        """public abstract boolean com.badlogic.gdx.audio.Music.isLooping()"""
        pass

    @abstractmethod
    def setVolume(self, arg0: float):
        """public abstract void com.badlogic.gdx.audio.Music.setVolume(float)"""
        pass

    @abstractmethod
    def getVolume(self, ):
        """public abstract float com.badlogic.gdx.audio.Music.getVolume()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.audio.Music.dispose()"""
        pass

    @abstractmethod
    def stop(self, ):
        """public abstract void com.badlogic.gdx.audio.Music.stop()"""
        pass

    @abstractmethod
    def setOnCompletionListener(self, arg0: 'OnCompletionListener'):
        """public abstract void com.badlogic.gdx.audio.Music.setOnCompletionListener(com.badlogic.gdx.audio.Music$OnCompletionListener)"""
        pass

    @abstractmethod
    def setPan(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.audio.Music.setPan(float,float)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.audio.AudioDevice
import com.badlogic.gdx.audio.AudioDevice as __AudioDevice
__AudioDevice = __AudioDevice
from builtins import float
from abc import abstractmethod, ABC
from builtins import int
 
class AudioDevice(ABC):
    """com.badlogic.gdx.audio.AudioDevice"""
 
    @staticmethod
    def __wrap(java_value: __AudioDevice) -> 'AudioDevice':
        return AudioDevice(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AudioDevice):
        """
        Dynamic initializer for AudioDevice.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def pause(self, ):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.pause()"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.dispose()"""
        pass

    @abstractmethod
    def isMono(self, ):
        """public abstract boolean com.badlogic.gdx.audio.AudioDevice.isMono()"""
        pass

    @abstractmethod
    def getLatency(self, ):
        """public abstract int com.badlogic.gdx.audio.AudioDevice.getLatency()"""
        pass

    @abstractmethod
    def writeSamples(self, arg0: 'float', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.writeSamples(float[],int,int)"""
        pass

    @abstractmethod
    def writeSamples(self, arg0: 'short', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.writeSamples(short[],int,int)"""
        pass

    @abstractmethod
    def setVolume(self, arg0: float):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.setVolume(float)"""
        pass

    @abstractmethod
    def resume(self, ):
        """public abstract void com.badlogic.gdx.audio.AudioDevice.resume()"""
        pass