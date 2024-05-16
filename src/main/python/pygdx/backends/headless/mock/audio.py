from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.audio.Music as _Music
_Music = _Music
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.backends.headless.mock.audio.MockAudio as _MockAudio
_MockAudio = _MockAudio
import com.badlogic.gdx.audio.AudioRecorder as _AudioRecorder
_AudioRecorder = _AudioRecorder
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.audio.Sound as _Sound
_Sound = _Sound
from typing import List
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.audio.AudioDevice as _AudioDevice
_AudioDevice = _AudioDevice
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockAudio():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudio"""
 
    @staticmethod
    def _wrap(java_value: _MockAudio) -> 'MockAudio':
        return MockAudio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockAudio):
        """
        Dynamic initializer for MockAudio.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockAudio__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockAudio__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def switchOutputDevice(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudio.switchOutputDevice(java.lang.String)"""
        return bool._wrap(super(_MockAudio, self).switchOutputDevice(arg0))

    @overload
    def newAudioRecorder(self, arg0: int, arg1: bool) -> 'audio.AudioRecorder':
        """public com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioRecorder(int,boolean)"""
        return 'audio.AudioRecorder'._wrap(super(_MockAudio, self).newAudioRecorder(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def newSound(self, arg0: 'FileHandle') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newSound(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Sound'._wrap(super(_MockAudio, self).newSound(arg0))

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

    @override
    @overload
    def getAvailableOutputDevices(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.backends.headless.mock.audio.MockAudio.getAvailableOutputDevices()"""
        return List[str]._wrap(super(MockAudio, self).getAvailableOutputDevices())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMusic(self, arg0: 'FileHandle') -> 'audio.Music':
        """public com.badlogic.gdx.audio.Music com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Music'._wrap(super(_MockAudio, self).newMusic(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = _MockAudio()
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = _MockAudio()
        self.__wrapper = val

    @overload
    def newAudioDevice(self, arg0: int, arg1: bool) -> 'audio.AudioDevice':
        """public com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioDevice(int,boolean)"""
        return 'audio.AudioDevice'._wrap(super(_MockAudio, self).newAudioDevice(_int.valueOf(arg0), _boolean.valueOf(arg1)))

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

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudio
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.audio.Music as _Music
_Music = _Music
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.backends.headless.mock.audio.MockAudio as _MockAudio
_MockAudio = _MockAudio
import com.badlogic.gdx.audio.AudioRecorder as _AudioRecorder
_AudioRecorder = _AudioRecorder
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.audio.Sound as _Sound
_Sound = _Sound
from typing import List
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.audio.AudioDevice as _AudioDevice
_AudioDevice = _AudioDevice
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockAudio():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudio"""
 
    @staticmethod
    def _wrap(java_value: _MockAudio) -> 'MockAudio':
        return MockAudio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockAudio):
        """
        Dynamic initializer for MockAudio.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockAudio__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockAudio__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def switchOutputDevice(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudio.switchOutputDevice(java.lang.String)"""
        return bool._wrap(super(_MockAudio, self).switchOutputDevice(arg0))

    @overload
    def newAudioRecorder(self, arg0: int, arg1: bool) -> 'audio.AudioRecorder':
        """public com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioRecorder(int,boolean)"""
        return 'audio.AudioRecorder'._wrap(super(_MockAudio, self).newAudioRecorder(_int.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def newSound(self, arg0: 'FileHandle') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newSound(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Sound'._wrap(super(_MockAudio, self).newSound(arg0))

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

    @override
    @overload
    def getAvailableOutputDevices(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.backends.headless.mock.audio.MockAudio.getAvailableOutputDevices()"""
        return List[str]._wrap(super(MockAudio, self).getAvailableOutputDevices())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMusic(self, arg0: 'FileHandle') -> 'audio.Music':
        """public com.badlogic.gdx.audio.Music com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Music'._wrap(super(_MockAudio, self).newMusic(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = _MockAudio()
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = _MockAudio()
        self.__wrapper = val

    @overload
    def newAudioDevice(self, arg0: int, arg1: bool) -> 'audio.AudioDevice':
        """public com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioDevice(int,boolean)"""
        return 'audio.AudioDevice'._wrap(super(_MockAudio, self).newAudioDevice(_int.valueOf(arg0), _boolean.valueOf(arg1)))

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

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudio 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockMusic
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.backends.headless.mock.audio.MockMusic as _MockMusic
_MockMusic = _MockMusic
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import audio
except ImportError:
    audio = _import_once("pygdx.audio")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockMusic():
    """com.badlogic.gdx.backends.headless.mock.audio.MockMusic"""
 
    @staticmethod
    def _wrap(java_value: _MockMusic) -> 'MockMusic':
        return MockMusic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockMusic):
        """
        Dynamic initializer for MockMusic.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockMusic__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockMusic__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setVolume(float)"""
        super(_MockMusic, self).setVolume(_float.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setPosition(float)"""
        super(_MockMusic, self).setPosition(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.pause()"""
        super(MockMusic, self).pause()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def play(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.play()"""
        super(MockMusic, self).play()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isPlaying(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockMusic.isPlaying()"""
        return bool._wrap(super(MockMusic, self).isPlaying())

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
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockMusic()"""
        val = _MockMusic()
        self.__wrapper = val

    @override
    @overload
    def setLooping(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setLooping(boolean)"""
        super(_MockMusic, self).setLooping(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockMusic()"""
        val = _MockMusic()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setPan(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setPan(float,float)"""
        super(_MockMusic, self).setPan(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getVolume(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.audio.MockMusic.getVolume()"""
        return float._wrap(super(MockMusic, self).getVolume())

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.stop()"""
        super(MockMusic, self).stop()

    @override
    @overload
    def isLooping(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockMusic.isLooping()"""
        return bool._wrap(super(MockMusic, self).isLooping())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.dispose()"""
        super(MockMusic, self).dispose()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPosition(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.audio.MockMusic.getPosition()"""
        return float._wrap(super(MockMusic, self).getPosition())

    @override
    @overload
    def setOnCompletionListener(self, arg0: 'OnCompletionListener'):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setOnCompletionListener(com.badlogic.gdx.audio.Music$OnCompletionListener)"""
        super(_MockMusic, self).setOnCompletionListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder as _MockAudioRecorder
_MockAudioRecorder = _MockAudioRecorder
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockAudioRecorder():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder"""
 
    @staticmethod
    def _wrap(java_value: _MockAudioRecorder) -> 'MockAudioRecorder':
        return MockAudioRecorder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockAudioRecorder):
        """
        Dynamic initializer for MockAudioRecorder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockAudioRecorder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockAudioRecorder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder()"""
        val = _MockAudioRecorder()
        self.__wrapper = val

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

    @override
    @overload
    def read(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder.read(short[],int,int)"""
        super(_MockAudioRecorder, self).read(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder.dispose()"""
        super(MockAudioRecorder, self).dispose()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder()"""
        val = _MockAudioRecorder()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice as _MockAudioDevice
_MockAudioDevice = _MockAudioDevice
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockAudioDevice():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice"""
 
    @staticmethod
    def _wrap(java_value: _MockAudioDevice) -> 'MockAudioDevice':
        return MockAudioDevice(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockAudioDevice):
        """
        Dynamic initializer for MockAudioDevice.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockAudioDevice__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockAudioDevice__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.pause()"""
        super(MockAudioDevice, self).pause()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice()"""
        val = _MockAudioDevice()
        self.__wrapper = val

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

    @override
    @overload
    def writeSamples(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.writeSamples(float[],int,int)"""
        super(_MockAudioDevice, self).writeSamples(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isMono(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.isMono()"""
        return bool._wrap(super(MockAudioDevice, self).isMono())

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.setVolume(float)"""
        super(_MockAudioDevice, self).setVolume(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.dispose()"""
        super(MockAudioDevice, self).dispose()

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

    @override
    @overload
    def writeSamples(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.writeSamples(short[],int,int)"""
        super(_MockAudioDevice, self).writeSamples(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLatency(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.getLatency()"""
        return int._wrap(super(MockAudioDevice, self).getLatency())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice()"""
        val = _MockAudioDevice()
        self.__wrapper = val

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.resume()"""
        super(MockAudioDevice, self).resume()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockSound
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.backends.headless.mock.audio.MockSound as _MockSound
_MockSound = _MockSound
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockSound():
    """com.badlogic.gdx.backends.headless.mock.audio.MockSound"""
 
    @staticmethod
    def _wrap(java_value: _MockSound) -> 'MockSound':
        return MockSound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockSound):
        """
        Dynamic initializer for MockSound.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockSound__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockSound__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setLooping(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setLooping(long,boolean)"""
        super(_MockSound, self).setLooping(_long.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def pause(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.pause(long)"""
        super(_MockSound, self).pause(_long.valueOf(arg0))

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.pause()"""
        super(MockSound, self).pause()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.dispose()"""
        super(MockSound, self).dispose()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.resume()"""
        super(MockSound, self).resume()

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.stop()"""
        super(MockSound, self).stop()

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

    @override
    @overload
    def resume(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.resume(long)"""
        super(_MockSound, self).resume(_long.valueOf(arg0))

    @override
    @overload
    def loop(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop()"""
        return int._wrap(super(MockSound, self).loop())

    @override
    @overload
    def setPitch(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setPitch(long,float)"""
        super(_MockSound, self).setPitch(_long.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def setPan(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setPan(long,float,float)"""
        super(_MockSound, self).setPan(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def loop(self, arg0: float, arg1: float, arg2: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop(float,float,float)"""
        return int._wrap(super(_MockSound, self).loop(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockSound()"""
        val = _MockSound()
        self.__wrapper = val

    @override
    @overload
    def setVolume(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setVolume(long,float)"""
        super(_MockSound, self).setVolume(_long.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def play(self, arg0: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play(float)"""
        return int._wrap(super(_MockSound, self).play(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def loop(self, arg0: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop(float)"""
        return int._wrap(super(_MockSound, self).loop(_float.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def stop(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.stop(long)"""
        super(_MockSound, self).stop(_long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockSound()"""
        val = _MockSound()
        self.__wrapper = val

    @overload
    def play(self, arg0: float, arg1: float, arg2: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play(float,float,float)"""
        return int._wrap(super(_MockSound, self).play(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def play(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play()"""
        return int._wrap(super(MockSound, self).play())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())