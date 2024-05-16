from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as _DefensiveCircleFormationPattern
_DefensiveCircleFormationPattern = _DefensiveCircleFormationPattern
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefensiveCircleFormationPattern():
    """com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern"""
 
    @staticmethod
    def _wrap(java_value: _DefensiveCircleFormationPattern) -> 'DefensiveCircleFormationPattern':
        return DefensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefensiveCircleFormationPattern):
        """
        Dynamic initializer for DefensiveCircleFormationPattern.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefensiveCircleFormationPattern__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefensiveCircleFormationPattern__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(_DefensiveCircleFormationPattern, self).setNumberOfSlots(_int.valueOf(arg0))

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
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool._wrap(super(_DefensiveCircleFormationPattern, self).supportsSlots(_int.valueOf(arg0)))

    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'._wrap(super(_DefensiveCircleFormationPattern, self).calculateSlotLocation(arg0, _int.valueOf(arg1)))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern(float)"""
        val = _DefensiveCircleFormationPattern(_float.valueOf(arg0))
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as _DefensiveCircleFormationPattern
_DefensiveCircleFormationPattern = _DefensiveCircleFormationPattern
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefensiveCircleFormationPattern():
    """com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern"""
 
    @staticmethod
    def _wrap(java_value: _DefensiveCircleFormationPattern) -> 'DefensiveCircleFormationPattern':
        return DefensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefensiveCircleFormationPattern):
        """
        Dynamic initializer for DefensiveCircleFormationPattern.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefensiveCircleFormationPattern__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefensiveCircleFormationPattern__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(_DefensiveCircleFormationPattern, self).setNumberOfSlots(_int.valueOf(arg0))

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
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool._wrap(super(_DefensiveCircleFormationPattern, self).supportsSlots(_int.valueOf(arg0)))

    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'._wrap(super(_DefensiveCircleFormationPattern, self).calculateSlotLocation(arg0, _int.valueOf(arg1)))

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
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern(float)"""
        val = _DefensiveCircleFormationPattern(_float.valueOf(arg0))
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern as _OffensiveCircleFormationPattern
_OffensiveCircleFormationPattern = _OffensiveCircleFormationPattern
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as _DefensiveCircleFormationPattern
_DefensiveCircleFormationPattern = _DefensiveCircleFormationPattern
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OffensiveCircleFormationPattern():
    """com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern"""
 
    @staticmethod
    def _wrap(java_value: _OffensiveCircleFormationPattern) -> 'OffensiveCircleFormationPattern':
        return OffensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OffensiveCircleFormationPattern):
        """
        Dynamic initializer for OffensiveCircleFormationPattern.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OffensiveCircleFormationPattern__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OffensiveCircleFormationPattern__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'._wrap(super(_OffensiveCircleFormationPattern, self).calculateSlotLocation(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(_DefensiveCircleFormationPattern, self).setNumberOfSlots(_int.valueOf(arg0))

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
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool._wrap(super(_DefensiveCircleFormationPattern, self).supportsSlots(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern(float)"""
        val = _OffensiveCircleFormationPattern(_float.valueOf(arg0))
        self.__wrapper = val

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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