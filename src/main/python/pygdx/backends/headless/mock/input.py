from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
import com.badlogic.gdx.Input as __Input_Orientation
__Orientation = __Input_Orientation.Orientation
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.InputProcessor as __InputProcessor
__InputProcessor = __InputProcessor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.backends.headless.mock.input.MockInput as __MockInput
__MockInput = __MockInput
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MockInput():
    """com.badlogic.gdx.backends.headless.mock.input.MockInput"""
 
    @staticmethod
    def __wrap(java_value: __MockInput) -> 'MockInput':
        return MockInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockInput):
        """
        Dynamic initializer for MockInput.
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
 
    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyJustPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isKeyJustPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__MockInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0), arg1)

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY(int)"""
        return int.__wrap(super(__MockInput, self).getY(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,int,boolean)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,boolean)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX()"""
        return int.__wrap(super(MockInput, self).getDeltaX())

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeX()"""
        return float.__wrap(super(MockInput, self).getGyroscopeX())

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchMenuKey(boolean)"""
        super(__MockInput, self).setCatchMenuKey(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = __MockInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.input.MockInput.getCurrentEventTime()"""
        return int.__wrap(super(MockInput, self).getCurrentEventTime())

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.backends.headless.mock.input.MockInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'.__wrap(super(MockInput, self).getNativeOrientation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchBackKey()"""
        return bool.__wrap(super(MockInput, self).isCatchBackKey())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = __MockInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool.__wrap(super(__MockInput, self).isPeripheralAvailable(arg0))

    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerX()"""
        return float.__wrap(super(MockInput, self).getAccelerometerX())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getMaxPointers()"""
        return int.__wrap(super(MockInput, self).getMaxPointers())

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeZ()"""
        return float.__wrap(super(MockInput, self).getGyroscopeZ())

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY()"""
        return int.__wrap(super(MockInput, self).getDeltaY())

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isButtonPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean)"""
        super(__MockInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerZ()"""
        return float.__wrap(super(MockInput, self).getAccelerometerZ())

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX(int)"""
        return int.__wrap(super(__MockInput, self).getX(__int.valueOf(arg0)))

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX(int)"""
        return int.__wrap(super(__MockInput, self).getDeltaX(__int.valueOf(arg0)))

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY(int)"""
        return int.__wrap(super(__MockInput, self).getDeltaY(__int.valueOf(arg0)))

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchBackKey(boolean)"""
        super(__MockInput, self).setCatchBackKey(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched(int)"""
        return bool.__wrap(super(__MockInput, self).isTouched(__int.valueOf(arg0)))

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotation()"""
        return int.__wrap(super(MockInput, self).getRotation())

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.backends.headless.mock.input.MockInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'.__wrap(super(MockInput, self).getInputProcessor())

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCursorCatched()"""
        return bool.__wrap(super(MockInput, self).isCursorCatched())

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0))

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorCatched(boolean)"""
        super(__MockInput, self).setCursorCatched(__boolean.valueOf(arg0))

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isKeyPressed(__int.valueOf(arg0)))

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAzimuth()"""
        return float.__wrap(super(MockInput, self).getAzimuth())

    @override
    @overload
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotationMatrix(float[])"""
        super(__MockInput, self).getRotationMatrix(arg0)

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchKey(int)"""
        return bool.__wrap(super(__MockInput, self).isCatchKey(__int.valueOf(arg0)))

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeY()"""
        return float.__wrap(super(MockInput, self).getGyroscopeY())

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(__MockInput, self).setInputProcessor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonJustPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isButtonJustPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchKey(int,boolean)"""
        super(__MockInput, self).setCatchKey(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY()"""
        return int.__wrap(super(MockInput, self).getY())

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPitch()"""
        return float.__wrap(super(MockInput, self).getPitch())

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched()"""
        return bool.__wrap(super(MockInput, self).isTouched())

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.justTouched()"""
        return bool.__wrap(super(MockInput, self).justTouched())

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure(int)"""
        return float.__wrap(super(__MockInput, self).getPressure(__int.valueOf(arg0)))

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX()"""
        return int.__wrap(super(MockInput, self).getX())

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getRoll()"""
        return float.__wrap(super(MockInput, self).getRoll())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(__MockInput, self).vibrate(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure()"""
        return float.__wrap(super(MockInput, self).getPressure())

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(__MockInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerY()"""
        return float.__wrap(super(MockInput, self).getAccelerometerY())

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchMenuKey()"""
        return bool.__wrap(super(MockInput, self).isCatchMenuKey())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorPosition(int,int)"""
        super(__MockInput, self).setCursorPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__MockInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.input.MockInput
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
import com.badlogic.gdx.Input as __Input_Orientation
__Orientation = __Input_Orientation.Orientation
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.InputProcessor as __InputProcessor
__InputProcessor = __InputProcessor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.backends.headless.mock.input.MockInput as __MockInput
__MockInput = __MockInput
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MockInput():
    """com.badlogic.gdx.backends.headless.mock.input.MockInput"""
 
    @staticmethod
    def __wrap(java_value: __MockInput) -> 'MockInput':
        return MockInput(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MockInput):
        """
        Dynamic initializer for MockInput.
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
 
    @overload
    def isKeyJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyJustPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isKeyJustPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool, arg1: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__MockInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0), arg1)

    @overload
    def getY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY(int)"""
        return int.__wrap(super(__MockInput, self).getY(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def vibrate(self, arg0: int, arg1: int, arg2: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,int,boolean)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))

    @override
    @overload
    def vibrate(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int,boolean)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getDeltaX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX()"""
        return int.__wrap(super(MockInput, self).getDeltaX())

    @override
    @overload
    def getGyroscopeX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeX()"""
        return float.__wrap(super(MockInput, self).getGyroscopeX())

    @override
    @overload
    def setCatchMenuKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchMenuKey(boolean)"""
        super(__MockInput, self).setCatchMenuKey(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = __MockInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCurrentEventTime(self) -> int:
        """public long com.badlogic.gdx.backends.headless.mock.input.MockInput.getCurrentEventTime()"""
        return int.__wrap(super(MockInput, self).getCurrentEventTime())

    @override
    @overload
    def getNativeOrientation(self) -> 'pygdx.Input$Orientation':
        """public com.badlogic.gdx.Input$Orientation com.badlogic.gdx.backends.headless.mock.input.MockInput.getNativeOrientation()"""
        return 'pygdx.Input$Orientation'.__wrap(super(MockInput, self).getNativeOrientation())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isCatchBackKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchBackKey()"""
        return bool.__wrap(super(MockInput, self).isCatchBackKey())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.mock.input.MockInput()"""
        val = __MockInput()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isPeripheralAvailable(self, arg0: 'Peripheral') -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isPeripheralAvailable(com.badlogic.gdx.Input$Peripheral)"""
        return bool.__wrap(super(__MockInput, self).isPeripheralAvailable(arg0))

    @override
    @overload
    def getAccelerometerX(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerX()"""
        return float.__wrap(super(MockInput, self).getAccelerometerX())

    @override
    @overload
    def getMaxPointers(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getMaxPointers()"""
        return int.__wrap(super(MockInput, self).getMaxPointers())

    @override
    @overload
    def getGyroscopeZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeZ()"""
        return float.__wrap(super(MockInput, self).getGyroscopeZ())

    @override
    @overload
    def getDeltaY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY()"""
        return int.__wrap(super(MockInput, self).getDeltaY())

    @overload
    def isButtonPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isButtonPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setOnscreenKeyboardVisible(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setOnscreenKeyboardVisible(boolean)"""
        super(__MockInput, self).setOnscreenKeyboardVisible(__boolean.valueOf(arg0))

    @override
    @overload
    def getAccelerometerZ(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerZ()"""
        return float.__wrap(super(MockInput, self).getAccelerometerZ())

    @overload
    def getX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX(int)"""
        return int.__wrap(super(__MockInput, self).getX(__int.valueOf(arg0)))

    @overload
    def getDeltaX(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaX(int)"""
        return int.__wrap(super(__MockInput, self).getDeltaX(__int.valueOf(arg0)))

    @overload
    def getDeltaY(self, arg0: int) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getDeltaY(int)"""
        return int.__wrap(super(__MockInput, self).getDeltaY(__int.valueOf(arg0)))

    @override
    @overload
    def setCatchBackKey(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchBackKey(boolean)"""
        super(__MockInput, self).setCatchBackKey(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isTouched(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched(int)"""
        return bool.__wrap(super(__MockInput, self).isTouched(__int.valueOf(arg0)))

    @override
    @overload
    def getRotation(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotation()"""
        return int.__wrap(super(MockInput, self).getRotation())

    @override
    @overload
    def getInputProcessor(self) -> 'pygdx.InputProcessor':
        """public com.badlogic.gdx.InputProcessor com.badlogic.gdx.backends.headless.mock.input.MockInput.getInputProcessor()"""
        return 'pygdx.InputProcessor'.__wrap(super(MockInput, self).getInputProcessor())

    @override
    @overload
    def isCursorCatched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCursorCatched()"""
        return bool.__wrap(super(MockInput, self).isCursorCatched())

    @override
    @overload
    def vibrate(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(int)"""
        super(__MockInput, self).vibrate(__int.valueOf(arg0))

    @override
    @overload
    def setCursorCatched(self, arg0: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorCatched(boolean)"""
        super(__MockInput, self).setCursorCatched(__boolean.valueOf(arg0))

    @overload
    def isKeyPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isKeyPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isKeyPressed(__int.valueOf(arg0)))

    @override
    @overload
    def getAzimuth(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAzimuth()"""
        return float.__wrap(super(MockInput, self).getAzimuth())

    @override
    @overload
    def getRotationMatrix(self, arg0: 'float'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getRotationMatrix(float[])"""
        super(__MockInput, self).getRotationMatrix(arg0)

    @overload
    def isCatchKey(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchKey(int)"""
        return bool.__wrap(super(__MockInput, self).isCatchKey(__int.valueOf(arg0)))

    @override
    @overload
    def getGyroscopeY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getGyroscopeY()"""
        return float.__wrap(super(MockInput, self).getGyroscopeY())

    @override
    @overload
    def setInputProcessor(self, arg0: 'InputProcessor'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setInputProcessor(com.badlogic.gdx.InputProcessor)"""
        super(__MockInput, self).setInputProcessor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isButtonJustPressed(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isButtonJustPressed(int)"""
        return bool.__wrap(super(__MockInput, self).isButtonJustPressed(__int.valueOf(arg0)))

    @override
    @overload
    def setCatchKey(self, arg0: int, arg1: bool):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCatchKey(int,boolean)"""
        super(__MockInput, self).setCatchKey(__int.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getY(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getY()"""
        return int.__wrap(super(MockInput, self).getY())

    @override
    @overload
    def getPitch(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPitch()"""
        return float.__wrap(super(MockInput, self).getPitch())

    @override
    @overload
    def isTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isTouched()"""
        return bool.__wrap(super(MockInput, self).isTouched())

    @override
    @overload
    def justTouched(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.justTouched()"""
        return bool.__wrap(super(MockInput, self).justTouched())

    @overload
    def getPressure(self, arg0: int) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure(int)"""
        return float.__wrap(super(__MockInput, self).getPressure(__int.valueOf(arg0)))

    @override
    @overload
    def getX(self) -> int:
        """public int com.badlogic.gdx.backends.headless.mock.input.MockInput.getX()"""
        return int.__wrap(super(MockInput, self).getX())

    @override
    @overload
    def getRoll(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getRoll()"""
        return float.__wrap(super(MockInput, self).getRoll())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def vibrate(self, arg0: 'VibrationType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.vibrate(com.badlogic.gdx.Input$VibrationType)"""
        super(__MockInput, self).vibrate(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPressure(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getPressure()"""
        return float.__wrap(super(MockInput, self).getPressure())

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String)"""
        super(__MockInput, self).getTextInput(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getAccelerometerY(self) -> float:
        """public float com.badlogic.gdx.backends.headless.mock.input.MockInput.getAccelerometerY()"""
        return float.__wrap(super(MockInput, self).getAccelerometerY())

    @override
    @overload
    def isCatchMenuKey(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.mock.input.MockInput.isCatchMenuKey()"""
        return bool.__wrap(super(MockInput, self).isCatchMenuKey())

    @override
    @overload
    def setCursorPosition(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.setCursorPosition(int,int)"""
        super(__MockInput, self).setCursorPosition(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getTextInput(self, arg0: 'TextInputListener', arg1: str, arg2: str, arg3: str, arg4: 'OnscreenKeyboardType'):
        """public void com.badlogic.gdx.backends.headless.mock.input.MockInput.getTextInput(com.badlogic.gdx.Input$TextInputListener,java.lang.String,java.lang.String,java.lang.String,com.badlogic.gdx.Input$OnscreenKeyboardType)"""
        super(__MockInput, self).getTextInput(arg0, arg1, arg2, arg3, arg4)

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.mock.input.MockInput