from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.video.VideoDecoder as __VideoDecoder_VideoDecoderBuffers
__VideoDecoderBuffers = __VideoDecoder_VideoDecoderBuffers.VideoDecoderBuffers
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class VideoDecoderBuffers():
    """com.badlogic.gdx.video.VideoDecoder.VideoDecoderBuffers"""
 
    @staticmethod
    def __wrap(java_value: __VideoDecoderBuffers) -> 'VideoDecoderBuffers':
        return VideoDecoderBuffers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VideoDecoderBuffers):
        """
        Dynamic initializer for VideoDecoderBuffers.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAudioChannels(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioChannels()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getAudioChannels())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAudioSampleRate(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioSampleRate()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getAudioSampleRate())

    @overload
    def getAudioBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioBuffer()"""
        return 'ByteBuffer'.__wrap(super(VideoDecoderBuffers, self).getAudioBuffer())

    @overload
    def getVideoBufferWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBufferWidth()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoBufferWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getVideoBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBuffer()"""
        return 'ByteBuffer'.__wrap(super(VideoDecoderBuffers, self).getVideoBuffer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoHeight()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoHeight())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoWidth()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.video.VideoDecoder as __VideoDecoder_VideoDecoderBuffers
__VideoDecoderBuffers = __VideoDecoder_VideoDecoderBuffers.VideoDecoderBuffers
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class VideoDecoderBuffers():
    """com.badlogic.gdx.video.VideoDecoder.VideoDecoderBuffers"""
 
    @staticmethod
    def __wrap(java_value: __VideoDecoderBuffers) -> 'VideoDecoderBuffers':
        return VideoDecoderBuffers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VideoDecoderBuffers):
        """
        Dynamic initializer for VideoDecoderBuffers.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getAudioChannels(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioChannels()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getAudioChannels())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getAudioSampleRate(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioSampleRate()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getAudioSampleRate())

    @overload
    def getAudioBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioBuffer()"""
        return 'ByteBuffer'.__wrap(super(VideoDecoderBuffers, self).getAudioBuffer())

    @overload
    def getVideoBufferWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBufferWidth()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoBufferWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getVideoBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBuffer()"""
        return 'ByteBuffer'.__wrap(super(VideoDecoderBuffers, self).getVideoBuffer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoHeight()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoHeight())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoWidth()"""
        return int.__wrap(super(VideoDecoderBuffers, self).getVideoWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers 
 
 
# CLASS: com.badlogic.gdx.video.VideoDecoder
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
from builtins import float
from typing import Any
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.video.VideoDecoder as __VideoDecoder_VideoDecoderBuffers
__VideoDecoderBuffers = __VideoDecoder_VideoDecoderBuffers.VideoDecoderBuffers
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
import com.badlogic.gdx.video.VideoDecoder as __VideoDecoder
__VideoDecoder = __VideoDecoder
from builtins import bool
from builtins import int
 
class VideoDecoder():
    """com.badlogic.gdx.video.VideoDecoder"""
 
    @staticmethod
    def __wrap(java_value: __VideoDecoder) -> 'VideoDecoder':
        return VideoDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VideoDecoder):
        """
        Dynamic initializer for VideoDecoder.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def updateAudioBuffer(self):
        """public native void com.badlogic.gdx.video.VideoDecoder.updateAudioBuffer()"""
        super(VideoDecoder, self).updateAudioBuffer()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.video.VideoDecoder.dispose()"""
        super(VideoDecoder, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def close(self):
        """public void com.badlogic.gdx.video.VideoDecoder.close()"""
        super(VideoDecoder, self).close()

    @overload
    def loadStream(self, arg0: Any) -> 'VideoDecoderBuffers':
        """public native com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers com.badlogic.gdx.video.VideoDecoder.loadStream(com.badlogic.gdx.video.VideoDecoder$VideoFileReader) throws java.lang.IllegalArgumentException,java.lang.Exception"""
        return 'VideoDecoderBuffers'.__wrap(super(__VideoDecoder, self).loadStream(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isBuffered(self) -> bool:
        """public native boolean com.badlogic.gdx.video.VideoDecoder.isBuffered()"""
        return bool.__wrap(super(VideoDecoder, self).isBuffered())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def setDebug(arg0: bool):
        """public static native void com.badlogic.gdx.video.VideoDecoder.setDebug(boolean)"""
        __VideoDecoder.setDebug(__boolean.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nextVideoFrame(self) -> 'ByteBuffer':
        """public native java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder.nextVideoFrame()"""
        return 'ByteBuffer'.__wrap(super(VideoDecoder, self).nextVideoFrame())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.VideoDecoder()"""
        val = __VideoDecoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.VideoDecoder()"""
        val = __VideoDecoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getCurrentFrameTimestamp(self) -> float:
        """public native double com.badlogic.gdx.video.VideoDecoder.getCurrentFrameTimestamp()"""
        return float.__wrap(super(VideoDecoder, self).getCurrentFrameTimestamp()) 
 
 
# CLASS: com.badlogic.gdx.video.CommonVideoPlayerDesktop
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import com.badlogic.gdx.video.CommonVideoPlayerDesktop as __CommonVideoPlayerDesktop
__CommonVideoPlayerDesktop = __CommonVideoPlayerDesktop
from builtins import type
from builtins import float
import com.badlogic.gdx.video.AbstractVideoPlayer as __AbstractVideoPlayer
__AbstractVideoPlayer = __AbstractVideoPlayer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class CommonVideoPlayerDesktop(ABC):
    """com.badlogic.gdx.video.CommonVideoPlayerDesktop"""
 
    @staticmethod
    def __wrap(java_value: __CommonVideoPlayerDesktop) -> 'CommonVideoPlayerDesktop':
        return CommonVideoPlayerDesktop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommonVideoPlayerDesktop):
        """
        Dynamic initializer for CommonVideoPlayerDesktop.
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
 
    @override
    @overload
    def getCurrentTimestamp(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getCurrentTimestamp()"""
        return int.__wrap(super(CommonVideoPlayerDesktop, self).getCurrentTimestamp())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.stop()"""
        super(CommonVideoPlayerDesktop, self).stop()

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setVolume(float)"""
        super(__CommonVideoPlayerDesktop, self).setVolume(__float.valueOf(arg0))

    @override
    @overload
    def isPlaying(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isPlaying()"""
        return bool.__wrap(super(CommonVideoPlayerDesktop, self).isPlaying())

    @override
    @overload
    def setOnVideoSizeListener(self, arg0: 'VideoSizeListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnVideoSizeListener(com.badlogic.gdx.video.VideoPlayer$VideoSizeListener)"""
        super(__CommonVideoPlayerDesktop, self).setOnVideoSizeListener(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoHeight()"""
        return int.__wrap(super(CommonVideoPlayerDesktop, self).getVideoHeight())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.resume()"""
        super(CommonVideoPlayerDesktop, self).resume()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.dispose()"""
        super(CommonVideoPlayerDesktop, self).dispose()

    @override
    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoWidth()"""
        return int.__wrap(super(CommonVideoPlayerDesktop, self).getVideoWidth())

    @override
    @overload
    def isLooping(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isLooping()"""
        return bool.__wrap(super(CommonVideoPlayerDesktop, self).isLooping())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getVolume(self) -> float:
        """public float com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVolume()"""
        return float.__wrap(super(CommonVideoPlayerDesktop, self).getVolume())

    @override
    @overload
    def update(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.update()"""
        return bool.__wrap(super(CommonVideoPlayerDesktop, self).update())

    @override
    @overload
    def isBuffered(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isBuffered()"""
        return bool.__wrap(super(CommonVideoPlayerDesktop, self).isBuffered())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setLooping(self, arg0: bool):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setLooping(boolean)"""
        super(__CommonVideoPlayerDesktop, self).setLooping(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.pause()"""
        super(CommonVideoPlayerDesktop, self).pause()

    @override
    @overload
    def setOnCompletionListener(self, arg0: 'CompletionListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnCompletionListener(com.badlogic.gdx.video.VideoPlayer$CompletionListener)"""
        super(__CommonVideoPlayerDesktop, self).setOnCompletionListener(arg0)

    @overload
    def play(self, arg0: 'FileHandle') -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.play(com.badlogic.gdx.files.FileHandle) throws java.io.FileNotFoundException"""
        return bool.__wrap(super(__CommonVideoPlayerDesktop, self).play(arg0))

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.video.AbstractVideoPlayer.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__AbstractVideoPlayer, self).setFilter(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = __CommonVideoPlayerDesktop()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.video.CommonVideoPlayerDesktop.getTexture()"""
        return 'graphics.Texture'.__wrap(super(CommonVideoPlayerDesktop, self).getTexture())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = __CommonVideoPlayerDesktop()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.video.FfMpeg
import com.badlogic.gdx.video.FfMpeg as __FfMpeg
__FfMpeg = __FfMpeg
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FfMpeg():
    """com.badlogic.gdx.video.FfMpeg"""
 
    @staticmethod
    def __wrap(java_value: __FfMpeg) -> 'FfMpeg':
        return FfMpeg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FfMpeg):
        """
        Dynamic initializer for FfMpeg.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isLoaded() -> bool:
        """public static boolean com.badlogic.gdx.video.FfMpeg.isLoaded()"""
        return bool.__wrap(__FfMpeg.isLoaded())

    @staticmethod
    @overload
    def loadLibraries() -> bool:
        """public static boolean com.badlogic.gdx.video.FfMpeg.loadLibraries()"""
        return bool.__wrap(__FfMpeg.loadLibraries())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.FfMpeg()"""
        val = __FfMpeg()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.FfMpeg()"""
        val = __FfMpeg()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def setLibraryFilePath(arg0: str):
        """public static void com.badlogic.gdx.video.FfMpeg.setLibraryFilePath(java.lang.String)"""
        __FfMpeg.setLibraryFilePath(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def setDebugLogging(arg0: bool):
        """public static void com.badlogic.gdx.video.FfMpeg.setDebugLogging(boolean)"""
        __FfMpeg.setDebugLogging(__boolean.valueOf(arg0))