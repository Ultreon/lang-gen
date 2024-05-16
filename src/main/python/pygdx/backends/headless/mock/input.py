from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.backends.headless.mock.input.MockInput as _MockInput
_MockInput = _MockInput
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.Input as _Input_Orientation
_Orientation = _Input_Orientation.Orientation
import com.badlogic.gdx.InputProcessor as _InputProcessor
_InputProcessor = _InputProcessor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockInput():
    """com.badlogic.gdx.backends.headless.mock.input.MockInput"""
 
    @staticmethod
    def _wrap(java_value: _MockInput) -> 'MockInput':
        return MockInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockInput):
        """
        Dynamic initializer for MockInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched(int)"""
        return bool._wrap(super(_MockInput, self).isTouched(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = _MockInput()
        self.__wrapper = val

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerZ()"""
        return float._wrap(super(MockInput, self).getAccelerometerZ())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getMaxPointers()"""
        return int._wrap(super(MockInput, self).getMaxPointers())

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonJustPressed(int)"""
        return bool._wrap(super(_MockInput, self).isButtonJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchMenuKey(boolean)"""
        super(_MockInput, self).setCatchMenuKey(_boolean.valueOf(arg0))

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(_MockInput, self).setInputProcessor(arg0)

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure()"""
        return float._wrap(super(MockInput, self).getPressure())

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
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotationMatrix(float[])"""
        super(_MockInput, self).getRotationMatrix(arg0)

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAzimuth()"""
        return float._wrap(super(MockInput, self).getAzimuth())

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerY()"""
        return float._wrap(super(MockInput, self).getAccelerometerY())

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY(int)"""
        return int._wrap(super(_MockInput, self).getDeltaY(_int.valueOf(arg0)))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,boolean)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotation()"""
        return int._wrap(super(MockInput, self).getRotation())

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchKey(int,boolean)"""
        super(_MockInput, self).setCatchKey(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.backends.headless.mock.input.MockInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'._wrap(super(MockInput, self).getNativeOrientation())

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonPressed(int)"""
        return bool._wrap(super(_MockInput, self).isButtonPressed(_int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean)"""
        super(_MockInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.backends.headless.mock.input.MockInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'._wrap(super(MockInput, self).getInputProcessor())

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_MockInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0), arg1)

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.input.MockInput.getCurrentEventTime()"""
        return int._wrap(super(MockInput, self).getCurrentEventTime())

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchBackKey()"""
        return bool._wrap(super(MockInput, self).isCatchBackKey())

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY()"""
        return int._wrap(super(MockInput, self).getY())

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCursorCatched()"""
        return bool._wrap(super(MockInput, self).isCursorCatched())

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchBackKey(boolean)"""
        super(_MockInput, self).setCatchBackKey(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,int,boolean)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = _MockInput()
        self.__wrapper = val

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(_MockInput, self).vibrate(arg0)

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_MockInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeY()"""
        return float._wrap(super(MockInput, self).getGyroscopeY())

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeZ()"""
        return float._wrap(super(MockInput, self).getGyroscopeZ())

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyPressed(int)"""
        return bool._wrap(super(_MockInput, self).isKeyPressed(_int.valueOf(arg0)))

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX(int)"""
        return int._wrap(super(_MockInput, self).getDeltaX(_int.valueOf(arg0)))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(_MockInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY(int)"""
        return int._wrap(super(_MockInput, self).getY(_int.valueOf(arg0)))

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY()"""
        return int._wrap(super(MockInput, self).getDeltaY())

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure(int)"""
        return float._wrap(super(_MockInput, self).getPressure(_int.valueOf(arg0)))

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchMenuKey()"""
        return bool._wrap(super(MockInput, self).isCatchMenuKey())

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyJustPressed(int)"""
        return bool._wrap(super(_MockInput, self).isKeyJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX()"""
        return int._wrap(super(MockInput, self).getX())

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPitch()"""
        return float._wrap(super(MockInput, self).getPitch())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorCatched(boolean)"""
        super(_MockInput, self).setCursorCatched(_boolean.valueOf(arg0))

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX(int)"""
        return int._wrap(super(_MockInput, self).getX(_int.valueOf(arg0)))

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getRoll()"""
        return float._wrap(super(MockInput, self).getRoll())

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchKey(int)"""
        return bool._wrap(super(_MockInput, self).isCatchKey(_int.valueOf(arg0)))

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool._wrap(super(_MockInput, self).isPeripheralAvailable(arg0))

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.justTouched()"""
        return bool._wrap(super(MockInput, self).justTouched())

    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerX()"""
        return float._wrap(super(MockInput, self).getAccelerometerX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched()"""
        return bool._wrap(super(MockInput, self).isTouched())

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeX()"""
        return float._wrap(super(MockInput, self).getGyroscopeX())

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX()"""
        return int._wrap(super(MockInput, self).getDeltaX())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorPosition(int,int)"""
        super(_MockInput, self).setCursorPosition(_int.valueOf(arg0), _int.valueOf(arg1))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.input.MockInput
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.backends.headless.mock.input.MockInput as _MockInput
_MockInput = _MockInput
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.Input as _Input_Orientation
_Orientation = _Input_Orientation.Orientation
import com.badlogic.gdx.InputProcessor as _InputProcessor
_InputProcessor = _InputProcessor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MockInput():
    """com.badlogic.gdx.backends.headless.mock.input.MockInput"""
 
    @staticmethod
    def _wrap(java_value: _MockInput) -> 'MockInput':
        return MockInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MockInput):
        """
        Dynamic initializer for MockInput.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MockInput__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MockInput__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched(int)"""
        return bool._wrap(super(_MockInput, self).isTouched(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = _MockInput()
        self.__wrapper = val

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerZ()"""
        return float._wrap(super(MockInput, self).getAccelerometerZ())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getMaxPointers()"""
        return int._wrap(super(MockInput, self).getMaxPointers())

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonJustPressed(int)"""
        return bool._wrap(super(_MockInput, self).isButtonJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchMenuKey(boolean)"""
        super(_MockInput, self).setCatchMenuKey(_boolean.valueOf(arg0))

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(_MockInput, self).setInputProcessor(arg0)

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure()"""
        return float._wrap(super(MockInput, self).getPressure())

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
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotationMatrix(float[])"""
        super(_MockInput, self).getRotationMatrix(arg0)

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAzimuth()"""
        return float._wrap(super(MockInput, self).getAzimuth())

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerY()"""
        return float._wrap(super(MockInput, self).getAccelerometerY())

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY(int)"""
        return int._wrap(super(_MockInput, self).getDeltaY(_int.valueOf(arg0)))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,boolean)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotation()"""
        return int._wrap(super(MockInput, self).getRotation())

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchKey(int,boolean)"""
        super(_MockInput, self).setCatchKey(_int.valueOf(arg0), _boolean.valueOf(arg1))

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.backends.headless.mock.input.MockInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'._wrap(super(MockInput, self).getNativeOrientation())

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonPressed(int)"""
        return bool._wrap(super(_MockInput, self).isButtonPressed(_int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean)"""
        super(_MockInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.backends.headless.mock.input.MockInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'._wrap(super(MockInput, self).getInputProcessor())

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_MockInput, self).setOnscreenKeyboardVisible(_boolean.valueOf(arg0), arg1)

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.input.MockInput.getCurrentEventTime()"""
        return int._wrap(super(MockInput, self).getCurrentEventTime())

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchBackKey()"""
        return bool._wrap(super(MockInput, self).isCatchBackKey())

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY()"""
        return int._wrap(super(MockInput, self).getY())

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCursorCatched()"""
        return bool._wrap(super(MockInput, self).isCursorCatched())

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchBackKey(boolean)"""
        super(_MockInput, self).setCatchBackKey(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,int,boolean)"""
        super(_MockInput, self).vibrate(_int.valueOf(arg0), _int.valueOf(arg1), _boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = _MockInput()
        self.__wrapper = val

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(_MockInput, self).vibrate(arg0)

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(_MockInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeY()"""
        return float._wrap(super(MockInput, self).getGyroscopeY())

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeZ()"""
        return float._wrap(super(MockInput, self).getGyroscopeZ())

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyPressed(int)"""
        return bool._wrap(super(_MockInput, self).isKeyPressed(_int.valueOf(arg0)))

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX(int)"""
        return int._wrap(super(_MockInput, self).getDeltaX(_int.valueOf(arg0)))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(_MockInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY(int)"""
        return int._wrap(super(_MockInput, self).getY(_int.valueOf(arg0)))

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY()"""
        return int._wrap(super(MockInput, self).getDeltaY())

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure(int)"""
        return float._wrap(super(_MockInput, self).getPressure(_int.valueOf(arg0)))

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchMenuKey()"""
        return bool._wrap(super(MockInput, self).isCatchMenuKey())

    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyJustPressed(int)"""
        return bool._wrap(super(_MockInput, self).isKeyJustPressed(_int.valueOf(arg0)))

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX()"""
        return int._wrap(super(MockInput, self).getX())

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPitch()"""
        return float._wrap(super(MockInput, self).getPitch())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorCatched(boolean)"""
        super(_MockInput, self).setCursorCatched(_boolean.valueOf(arg0))

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX(int)"""
        return int._wrap(super(_MockInput, self).getX(_int.valueOf(arg0)))

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getRoll()"""
        return float._wrap(super(MockInput, self).getRoll())

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchKey(int)"""
        return bool._wrap(super(_MockInput, self).isCatchKey(_int.valueOf(arg0)))

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool._wrap(super(_MockInput, self).isPeripheralAvailable(arg0))

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.justTouched()"""
        return bool._wrap(super(MockInput, self).justTouched())

    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerX()"""
        return float._wrap(super(MockInput, self).getAccelerometerX())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched()"""
        return bool._wrap(super(MockInput, self).isTouched())

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeX()"""
        return float._wrap(super(MockInput, self).getGyroscopeX())

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX()"""
        return int._wrap(super(MockInput, self).getDeltaX())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorPosition(int,int)"""
        super(_MockInput, self).setCursorPosition(_int.valueOf(arg0), _int.valueOf(arg1))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.input.MockInput