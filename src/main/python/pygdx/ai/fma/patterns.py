from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as __DefensiveCircleFormationPattern
__DefensiveCircleFormationPattern = __DefensiveCircleFormationPattern
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class DefensiveCircleFormationPattern(ai.__FormationPattern, fma.FormationPattern):
    """com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern"""
 
    @staticmethod
    def __wrap(java_value: __DefensiveCircleFormationPattern) -> 'DefensiveCircleFormationPattern':
        return DefensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefensiveCircleFormationPattern):
        """
        Dynamic initializer for DefensiveCircleFormationPattern.
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

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern(float)"""
        val = __DefensiveCircleFormationPattern(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(__DefensiveCircleFormationPattern, self).setNumberOfSlots(__int.valueOf(arg0))

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

    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'.__wrap(super(__DefensiveCircleFormationPattern, self).calculateSlotLocation(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool.__wrap(super(__DefensiveCircleFormationPattern, self).supportsSlots(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as __DefensiveCircleFormationPattern
__DefensiveCircleFormationPattern = __DefensiveCircleFormationPattern
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class DefensiveCircleFormationPattern(ai.__FormationPattern, fma.FormationPattern):
    """com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern"""
 
    @staticmethod
    def __wrap(java_value: __DefensiveCircleFormationPattern) -> 'DefensiveCircleFormationPattern':
        return DefensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefensiveCircleFormationPattern):
        """
        Dynamic initializer for DefensiveCircleFormationPattern.
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

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern(float)"""
        val = __DefensiveCircleFormationPattern(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(__DefensiveCircleFormationPattern, self).setNumberOfSlots(__int.valueOf(arg0))

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

    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'.__wrap(super(__DefensiveCircleFormationPattern, self).calculateSlotLocation(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool.__wrap(super(__DefensiveCircleFormationPattern, self).supportsSlots(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern 
 
 
# CLASS: com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern as __OffensiveCircleFormationPattern
__OffensiveCircleFormationPattern = __OffensiveCircleFormationPattern
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern as __DefensiveCircleFormationPattern
__DefensiveCircleFormationPattern = __DefensiveCircleFormationPattern
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class OffensiveCircleFormationPattern(__DefensiveCircleFormationPattern, DefensiveCircleFormationPattern):
    """com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern"""
 
    @staticmethod
    def __wrap(java_value: __OffensiveCircleFormationPattern) -> 'OffensiveCircleFormationPattern':
        return OffensiveCircleFormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OffensiveCircleFormationPattern):
        """
        Dynamic initializer for OffensiveCircleFormationPattern.
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
    def setNumberOfSlots(self, arg0: int):
        """public void com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.setNumberOfSlots(int)"""
        super(__DefensiveCircleFormationPattern, self).setNumberOfSlots(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern(float)"""
        val = __OffensiveCircleFormationPattern(__float.valueOf(arg0))
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def calculateSlotLocation(self, arg0: 'Location', arg1: int) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.patterns.OffensiveCircleFormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        return 'utils.Location'.__wrap(super(__OffensiveCircleFormationPattern, self).calculateSlotLocation(arg0, __int.valueOf(arg1)))

    @overload
    def supportsSlots(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.fma.patterns.DefensiveCircleFormationPattern.supportsSlots(int)"""
        return bool.__wrap(super(__DefensiveCircleFormationPattern, self).supportsSlots(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))