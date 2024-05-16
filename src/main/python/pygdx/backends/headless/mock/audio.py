from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.backends.headless.mock.audio.MockAudio as __MockAudio
__MockAudio = __MockAudio
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
import com.badlogic.gdx.audio.AudioRecorder as __AudioRecorder
__AudioRecorder = __AudioRecorder
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.audio.AudioDevice as __AudioDevice
__AudioDevice = __AudioDevice
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = __import_once__("pygdx.audio")

import java.lang.Integer as __int
import com.badlogic.gdx.audio.Music as __Music
__Music = __Music
from builtins import bool
from builtins import int
 
class MockAudio():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudio"""
 
    @staticmethod
    def __wrap(java_value: __MockAudio) -> 'MockAudio':
        return MockAudio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockAudio):
        """
        Dynamic initializer for MockAudio.
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
    def newAudioRecorder(self, arg0: int, arg1: bool) -> 'audio.AudioRecorder':
        """public com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioRecorder(int,boolean)"""
        return 'audio.AudioRecorder'.__wrap(super(__MockAudio, self).newAudioRecorder(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = __MockAudio()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getAvailableOutputDevices(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.backends.headless.mock.audio.MockAudio.getAvailableOutputDevices()"""
        return List[str].__wrap(super(MockAudio, self).getAvailableOutputDevices())

    @overload
    def newAudioDevice(self, arg0: int, arg1: bool) -> 'audio.AudioDevice':
        """public com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioDevice(int,boolean)"""
        return 'audio.AudioDevice'.__wrap(super(__MockAudio, self).newAudioDevice(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def newSound(self, arg0: 'FileHandle') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newSound(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Sound'.__wrap(super(__MockAudio, self).newSound(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMusic(self, arg0: 'FileHandle') -> 'audio.Music':
        """public com.badlogic.gdx.audio.Music com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Music'.__wrap(super(__MockAudio, self).newMusic(arg0))

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
    def switchOutputDevice(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudio.switchOutputDevice(java.lang.String)"""
        return bool.__wrap(super(__MockAudio, self).switchOutputDevice(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = __MockAudio()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudio
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.backends.headless.mock.audio.MockAudio as __MockAudio
__MockAudio = __MockAudio
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.audio.Sound as __Sound
__Sound = __Sound
import com.badlogic.gdx.audio.AudioRecorder as __AudioRecorder
__AudioRecorder = __AudioRecorder
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.audio.AudioDevice as __AudioDevice
__AudioDevice = __AudioDevice
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import audio
except ImportError:
    audio = __import_once__("pygdx.audio")

import java.lang.Integer as __int
import com.badlogic.gdx.audio.Music as __Music
__Music = __Music
from builtins import bool
from builtins import int
 
class MockAudio():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudio"""
 
    @staticmethod
    def __wrap(java_value: __MockAudio) -> 'MockAudio':
        return MockAudio(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockAudio):
        """
        Dynamic initializer for MockAudio.
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
    def newAudioRecorder(self, arg0: int, arg1: bool) -> 'audio.AudioRecorder':
        """public com.badlogic.gdx.audio.AudioRecorder com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioRecorder(int,boolean)"""
        return 'audio.AudioRecorder'.__wrap(super(__MockAudio, self).newAudioRecorder(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = __MockAudio()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getAvailableOutputDevices(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.backends.headless.mock.audio.MockAudio.getAvailableOutputDevices()"""
        return List[str].__wrap(super(MockAudio, self).getAvailableOutputDevices())

    @overload
    def newAudioDevice(self, arg0: int, arg1: bool) -> 'audio.AudioDevice':
        """public com.badlogic.gdx.audio.AudioDevice com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newAudioDevice(int,boolean)"""
        return 'audio.AudioDevice'.__wrap(super(__MockAudio, self).newAudioDevice(__int.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def newSound(self, arg0: 'FileHandle') -> 'audio.Sound':
        """public com.badlogic.gdx.audio.Sound com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newSound(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Sound'.__wrap(super(__MockAudio, self).newSound(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMusic(self, arg0: 'FileHandle') -> 'audio.Music':
        """public com.badlogic.gdx.audio.Music com.badlogic.gdx.backends.headless.mock.audio.MockAudio.newMusic(com.badlogic.gdx.files.FileHandle)"""
        return 'audio.Music'.__wrap(super(__MockAudio, self).newMusic(arg0))

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
    def switchOutputDevice(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudio.switchOutputDevice(java.lang.String)"""
        return bool.__wrap(super(__MockAudio, self).switchOutputDevice(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudio()"""
        val = __MockAudio()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudio 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice as __MockAudioDevice
__MockAudioDevice = __MockAudioDevice
from builtins import int
 
class MockAudioDevice():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice"""
 
    @staticmethod
    def __wrap(java_value: __MockAudioDevice) -> 'MockAudioDevice':
        return MockAudioDevice(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockAudioDevice):
        """
        Dynamic initializer for MockAudioDevice.
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
    def pause(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.pause()"""
        super(MockAudioDevice, self).pause()

    @override
    @overload
    def writeSamples(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.writeSamples(short[],int,int)"""
        super(__MockAudioDevice, self).writeSamples(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getLatency(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.getLatency()"""
        return int.__wrap(super(MockAudioDevice, self).getLatency())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.setVolume(float)"""
        super(__MockAudioDevice, self).setVolume(__float.valueOf(arg0))

    @override
    @overload
    def isMono(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.isMono()"""
        return bool.__wrap(super(MockAudioDevice, self).isMono())

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
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.dispose()"""
        super(MockAudioDevice, self).dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice()"""
        val = __MockAudioDevice()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice()"""
        val = __MockAudioDevice()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def writeSamples(self, arg0: 'float', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.writeSamples(float[],int,int)"""
        super(__MockAudioDevice, self).writeSamples(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioDevice.resume()"""
        super(MockAudioDevice, self).resume()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder as __MockAudioRecorder
__MockAudioRecorder = __MockAudioRecorder
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MockAudioRecorder():
    """com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder"""
 
    @staticmethod
    def __wrap(java_value: __MockAudioRecorder) -> 'MockAudioRecorder':
        return MockAudioRecorder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockAudioRecorder):
        """
        Dynamic initializer for MockAudioRecorder.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder.dispose()"""
        super(MockAudioRecorder, self).dispose()

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
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder()"""
        val = __MockAudioRecorder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder.read(short[],int,int)"""
        super(__MockAudioRecorder, self).read(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockAudioRecorder()"""
        val = __MockAudioRecorder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockMusic
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.backends.headless.mock.audio.MockMusic as __MockMusic
__MockMusic = __MockMusic
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import audio
except ImportError:
    audio = __import_once__("pygdx.audio")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MockMusic():
    """com.badlogic.gdx.backends.headless.mock.audio.MockMusic"""
 
    @staticmethod
    def __wrap(java_value: __MockMusic) -> 'MockMusic':
        return MockMusic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockMusic):
        """
        Dynamic initializer for MockMusic.
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
    def setLooping(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setLooping(boolean)"""
        super(__MockMusic, self).setLooping(__boolean.valueOf(arg0))

    @override
    @overload
    def setVolume(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setVolume(float)"""
        super(__MockMusic, self).setVolume(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockMusic()"""
        val = __MockMusic()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockMusic()"""
        val = __MockMusic()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def pause(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.pause()"""
        super(MockMusic, self).pause()

    @override
    @overload
    def isPlaying(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockMusic.isPlaying()"""
        return bool.__wrap(super(MockMusic, self).isPlaying())

    @override
    @overload
    def getVolume(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.audio.MockMusic.getVolume()"""
        return float.__wrap(super(MockMusic, self).getVolume())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setPosition(float)"""
        super(__MockMusic, self).setPosition(__float.valueOf(arg0))

    @override
    @overload
    def setOnCompletionListener(self, arg0: 'OnCompletionListener'):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setOnCompletionListener(com.badlogic.gdx.audio.Music$OnCompletionListener)"""
        super(__MockMusic, self).setOnCompletionListener(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setPan(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.setPan(float,float)"""
        super(__MockMusic, self).setPan(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getPosition(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.audio.MockMusic.getPosition()"""
        return float.__wrap(super(MockMusic, self).getPosition())

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
    def stop(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockMusic.stop()"""
        super(MockMusic, self).stop()

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
    def isLooping(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.audio.MockMusic.isLooping()"""
        return bool.__wrap(super(MockMusic, self).isLooping())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.audio.MockSound
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.backends.headless.mock.audio.MockSound as __MockSound
__MockSound = __MockSound
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MockSound():
    """com.badlogic.gdx.backends.headless.mock.audio.MockSound"""
 
    @staticmethod
    def __wrap(java_value: __MockSound) -> 'MockSound':
        return MockSound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockSound):
        """
        Dynamic initializer for MockSound.
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
    def setPan(self, arg0: int, arg1: float, arg2: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setPan(long,float,float)"""
        super(__MockSound, self).setPan(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def play(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play()"""
        return int.__wrap(super(MockSound, self).play())

    @override
    @overload
    def stop(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.stop(long)"""
        super(__MockSound, self).stop(__long.valueOf(arg0))

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

    @overload
    def play(self, arg0: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play(float)"""
        return int.__wrap(super(__MockSound, self).play(__float.valueOf(arg0)))

    @override
    @overload
    def stop(self):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.stop()"""
        super(MockSound, self).stop()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def loop(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop()"""
        return int.__wrap(super(MockSound, self).loop())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockSound()"""
        val = __MockSound()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def play(self, arg0: float, arg1: float, arg2: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.play(float,float,float)"""
        return int.__wrap(super(__MockSound, self).play(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setLooping(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setLooping(long,boolean)"""
        super(__MockSound, self).setLooping(__long.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def loop(self, arg0: float, arg1: float, arg2: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop(float,float,float)"""
        return int.__wrap(super(__MockSound, self).loop(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def resume(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.resume(long)"""
        super(__MockSound, self).resume(__long.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setVolume(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setVolume(long,float)"""
        super(__MockSound, self).setVolume(__long.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def pause(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.pause(long)"""
        super(__MockSound, self).pause(__long.valueOf(arg0))

    @override
    @overload
    def setPitch(self, arg0: int, arg1: float):
        """public void com.badlogic.gdx.backends.headless.mock.audio.MockSound.setPitch(long,float)"""
        super(__MockSound, self).setPitch(__long.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.audio.MockSound()"""
        val = __MockSound()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loop(self, arg0: float) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.audio.MockSound.loop(float)"""
        return int.__wrap(super(__MockSound, self).loop(__float.valueOf(arg0)))