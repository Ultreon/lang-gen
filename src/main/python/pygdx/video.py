from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.video.AbstractVideoPlayer as _AbstractVideoPlayer
_AbstractVideoPlayer = _AbstractVideoPlayer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.video.CommonVideoPlayerDesktop as _CommonVideoPlayerDesktop
_CommonVideoPlayerDesktop = _CommonVideoPlayerDesktop
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommonVideoPlayerDesktop():
    """com.badlogic.gdx.video.CommonVideoPlayerDesktop"""
 
    @staticmethod
    def _wrap(java_value: _CommonVideoPlayerDesktop) -> 'CommonVideoPlayerDesktop':
        return CommonVideoPlayerDesktop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommonVideoPlayerDesktop):
        """
        Dynamic initializer for CommonVideoPlayerDesktop.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommonVideoPlayerDesktop__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommonVideoPlayerDesktop__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.stop()"""
        super(CommonVideoPlayerDesktop, self).stop()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = _CommonVideoPlayerDesktop()
        self.__wrapper = val

    @override
    @overload
    def isLooping(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isLooping()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isLooping())

    @override
    @overload
    def isPlaying(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isPlaying()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isPlaying())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.video.AbstractVideoPlayer.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_AbstractVideoPlayer, self).setFilter(arg0, arg1)

    @override
    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoWidth()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getVideoWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isBuffered(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isBuffered()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isBuffered())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.video.CommonVideoPlayerDesktop.getTexture()"""
        return 'graphics.Texture'._wrap(super(CommonVideoPlayerDesktop, self).getTexture())

    @overload
    def play(self, arg0: 'FileHandle') -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.play(com.badlogic.gdx.files.FileHandle) throws java.io.FileNotFoundException"""
        return bool._wrap(super(_CommonVideoPlayerDesktop, self).play(arg0))

    @override
    @overload
    def getVolume(self) -> float:
        """public float com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVolume()"""
        return float._wrap(super(CommonVideoPlayerDesktop, self).getVolume())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = _CommonVideoPlayerDesktop()
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setOnCompletionListener(self, arg0: 'CompletionListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnCompletionListener(com.badlogic.gdx.video.VideoPlayer$CompletionListener)"""
        super(_CommonVideoPlayerDesktop, self).setOnCompletionListener(arg0)

    @override
    @overload
    def update(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.update()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).update())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoHeight()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getVideoHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.pause()"""
        super(CommonVideoPlayerDesktop, self).pause()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getCurrentTimestamp(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getCurrentTimestamp()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getCurrentTimestamp())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setLooping(self, arg0: bool):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setLooping(boolean)"""
        super(_CommonVideoPlayerDesktop, self).setLooping(_boolean.valueOf(arg0))

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setVolume(float)"""
        super(_CommonVideoPlayerDesktop, self).setVolume(_float.valueOf(arg0))

    @override
    @overload
    def setOnVideoSizeListener(self, arg0: 'VideoSizeListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnVideoSizeListener(com.badlogic.gdx.video.VideoPlayer$VideoSizeListener)"""
        super(_CommonVideoPlayerDesktop, self).setOnVideoSizeListener(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.video.CommonVideoPlayerDesktop
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.video.AbstractVideoPlayer as _AbstractVideoPlayer
_AbstractVideoPlayer = _AbstractVideoPlayer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.video.CommonVideoPlayerDesktop as _CommonVideoPlayerDesktop
_CommonVideoPlayerDesktop = _CommonVideoPlayerDesktop
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommonVideoPlayerDesktop():
    """com.badlogic.gdx.video.CommonVideoPlayerDesktop"""
 
    @staticmethod
    def _wrap(java_value: _CommonVideoPlayerDesktop) -> 'CommonVideoPlayerDesktop':
        return CommonVideoPlayerDesktop(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommonVideoPlayerDesktop):
        """
        Dynamic initializer for CommonVideoPlayerDesktop.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommonVideoPlayerDesktop__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommonVideoPlayerDesktop__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.stop()"""
        super(CommonVideoPlayerDesktop, self).stop()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = _CommonVideoPlayerDesktop()
        self.__wrapper = val

    @override
    @overload
    def isLooping(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isLooping()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isLooping())

    @override
    @overload
    def isPlaying(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isPlaying()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isPlaying())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.video.AbstractVideoPlayer.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(_AbstractVideoPlayer, self).setFilter(arg0, arg1)

    @override
    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoWidth()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getVideoWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def isBuffered(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.isBuffered()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).isBuffered())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.video.CommonVideoPlayerDesktop.getTexture()"""
        return 'graphics.Texture'._wrap(super(CommonVideoPlayerDesktop, self).getTexture())

    @overload
    def play(self, arg0: 'FileHandle') -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.play(com.badlogic.gdx.files.FileHandle) throws java.io.FileNotFoundException"""
        return bool._wrap(super(_CommonVideoPlayerDesktop, self).play(arg0))

    @override
    @overload
    def getVolume(self) -> float:
        """public float com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVolume()"""
        return float._wrap(super(CommonVideoPlayerDesktop, self).getVolume())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.CommonVideoPlayerDesktop()"""
        val = _CommonVideoPlayerDesktop()
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setOnCompletionListener(self, arg0: 'CompletionListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnCompletionListener(com.badlogic.gdx.video.VideoPlayer$CompletionListener)"""
        super(_CommonVideoPlayerDesktop, self).setOnCompletionListener(arg0)

    @override
    @overload
    def update(self) -> bool:
        """public boolean com.badlogic.gdx.video.CommonVideoPlayerDesktop.update()"""
        return bool._wrap(super(CommonVideoPlayerDesktop, self).update())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getVideoHeight()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getVideoHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.pause()"""
        super(CommonVideoPlayerDesktop, self).pause()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getCurrentTimestamp(self) -> int:
        """public int com.badlogic.gdx.video.CommonVideoPlayerDesktop.getCurrentTimestamp()"""
        return int._wrap(super(CommonVideoPlayerDesktop, self).getCurrentTimestamp())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setLooping(self, arg0: bool):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setLooping(boolean)"""
        super(_CommonVideoPlayerDesktop, self).setLooping(_boolean.valueOf(arg0))

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setVolume(float)"""
        super(_CommonVideoPlayerDesktop, self).setVolume(_float.valueOf(arg0))

    @override
    @overload
    def setOnVideoSizeListener(self, arg0: 'VideoSizeListener'):
        """public void com.badlogic.gdx.video.CommonVideoPlayerDesktop.setOnVideoSizeListener(com.badlogic.gdx.video.VideoPlayer$VideoSizeListener)"""
        super(_CommonVideoPlayerDesktop, self).setOnVideoSizeListener(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.video.CommonVideoPlayerDesktop 
 
 
# CLASS: com.badlogic.gdx.video.FfMpeg
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.video.FfMpeg as _FfMpeg
_FfMpeg = _FfMpeg
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FfMpeg():
    """com.badlogic.gdx.video.FfMpeg"""
 
    @staticmethod
    def _wrap(java_value: _FfMpeg) -> 'FfMpeg':
        return FfMpeg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FfMpeg):
        """
        Dynamic initializer for FfMpeg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FfMpeg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FfMpeg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.FfMpeg()"""
        val = _FfMpeg()
        self.__wrapper = val

    @staticmethod
    @overload
    def isLoaded() -> bool:
        """public static boolean com.badlogic.gdx.video.FfMpeg.isLoaded()"""
        return bool._wrap(_FfMpeg.isLoaded())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def loadLibraries() -> bool:
        """public static boolean com.badlogic.gdx.video.FfMpeg.loadLibraries()"""
        return bool._wrap(_FfMpeg.loadLibraries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.FfMpeg()"""
        val = _FfMpeg()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setLibraryFilePath(arg0: str):
        """public static void com.badlogic.gdx.video.FfMpeg.setLibraryFilePath(java.lang.String)"""
        _FfMpeg.setLibraryFilePath(arg0)

    @staticmethod
    @overload
    def setDebugLogging(arg0: bool):
        """public static void com.badlogic.gdx.video.FfMpeg.setDebugLogging(boolean)"""
        _FfMpeg.setDebugLogging(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.video.VideoDecoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.video.VideoDecoder as _VideoDecoder_VideoDecoderBuffers
_VideoDecoderBuffers = _VideoDecoder_VideoDecoderBuffers.VideoDecoderBuffers
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
from builtins import float
import java.lang.String as _String
_String = _String
from typing import Any
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.video.VideoDecoder as _VideoDecoder
_VideoDecoder = _VideoDecoder
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VideoDecoder():
    """com.badlogic.gdx.video.VideoDecoder"""
 
    @staticmethod
    def _wrap(java_value: _VideoDecoder) -> 'VideoDecoder':
        return VideoDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VideoDecoder):
        """
        Dynamic initializer for VideoDecoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VideoDecoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VideoDecoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def updateAudioBuffer(self):
        """public native void com.badlogic.gdx.video.VideoDecoder.updateAudioBuffer()"""
        super(VideoDecoder, self).updateAudioBuffer()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.video.VideoDecoder.dispose()"""
        super(VideoDecoder, self).dispose()

    @overload
    def close(self):
        """public void com.badlogic.gdx.video.VideoDecoder.close()"""
        super(VideoDecoder, self).close()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.video.VideoDecoder()"""
        val = _VideoDecoder()
        self.__wrapper = val

    @overload
    def nextVideoFrame(self) -> 'ByteBuffer':
        """public native java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder.nextVideoFrame()"""
        return 'ByteBuffer'._wrap(super(VideoDecoder, self).nextVideoFrame())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getCurrentFrameTimestamp(self) -> float:
        """public native double com.badlogic.gdx.video.VideoDecoder.getCurrentFrameTimestamp()"""
        return float._wrap(super(VideoDecoder, self).getCurrentFrameTimestamp())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.video.VideoDecoder()"""
        val = _VideoDecoder()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isBuffered(self) -> bool:
        """public native boolean com.badlogic.gdx.video.VideoDecoder.isBuffered()"""
        return bool._wrap(super(VideoDecoder, self).isBuffered())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def setDebug(arg0: bool):
        """public static native void com.badlogic.gdx.video.VideoDecoder.setDebug(boolean)"""
        _VideoDecoder.setDebug(_boolean.valueOf(arg0))

    @overload
    def loadStream(self, arg0: Any) -> 'VideoDecoderBuffers':
        """public native com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers com.badlogic.gdx.video.VideoDecoder.loadStream(com.badlogic.gdx.video.VideoDecoder$VideoFileReader) throws java.lang.IllegalArgumentException,java.lang.Exception"""
        return 'VideoDecoderBuffers'._wrap(super(_VideoDecoder, self).loadStream(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.video.VideoDecoder as _VideoDecoder_VideoDecoderBuffers
_VideoDecoderBuffers = _VideoDecoder_VideoDecoderBuffers.VideoDecoderBuffers
import java.lang.Object as _object
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class VideoDecoderBuffers():
    """com.badlogic.gdx.video.VideoDecoder.VideoDecoderBuffers"""
 
    @staticmethod
    def _wrap(java_value: _VideoDecoderBuffers) -> 'VideoDecoderBuffers':
        return VideoDecoderBuffers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _VideoDecoderBuffers):
        """
        Dynamic initializer for VideoDecoderBuffers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_VideoDecoderBuffers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_VideoDecoderBuffers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getVideoBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBuffer()"""
        return 'ByteBuffer'._wrap(super(VideoDecoderBuffers, self).getVideoBuffer())

    @overload
    def getVideoHeight(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoHeight()"""
        return int._wrap(super(VideoDecoderBuffers, self).getVideoHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getVideoWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoWidth()"""
        return int._wrap(super(VideoDecoderBuffers, self).getVideoWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getAudioSampleRate(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioSampleRate()"""
        return int._wrap(super(VideoDecoderBuffers, self).getAudioSampleRate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAudioChannels(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioChannels()"""
        return int._wrap(super(VideoDecoderBuffers, self).getAudioChannels())

    @overload
    def getAudioBuffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getAudioBuffer()"""
        return 'ByteBuffer'._wrap(super(VideoDecoderBuffers, self).getAudioBuffer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getVideoBufferWidth(self) -> int:
        """public int com.badlogic.gdx.video.VideoDecoder$VideoDecoderBuffers.getVideoBufferWidth()"""
        return int._wrap(super(VideoDecoderBuffers, self).getVideoBufferWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())