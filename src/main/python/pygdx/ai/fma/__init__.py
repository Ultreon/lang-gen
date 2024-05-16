from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy as _BoundedSlotAssignmentStrategy
_BoundedSlotAssignmentStrategy = _BoundedSlotAssignmentStrategy
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy as _SoftRoleSlotAssignmentStrategy
_SoftRoleSlotAssignmentStrategy = _SoftRoleSlotAssignmentStrategy
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoftRoleSlotAssignmentStrategy():
    """com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy"""
 
    @staticmethod
    def _wrap(java_value: _SoftRoleSlotAssignmentStrategy) -> 'SoftRoleSlotAssignmentStrategy':
        return SoftRoleSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoftRoleSlotAssignmentStrategy):
        """
        Dynamic initializer for SoftRoleSlotAssignmentStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoftRoleSlotAssignmentStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoftRoleSlotAssignmentStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(_BoundedSlotAssignmentStrategy, self).removeSlotAssignment(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'SlotCostProvider', arg1: float):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>,float)"""
        val = _SoftRoleSlotAssignmentStrategy(arg0, _float.valueOf(arg1))
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

    @overload
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int._wrap(super(_BoundedSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

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

    @override
    @overload
    def updateSlotAssignments(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        super(_SoftRoleSlotAssignmentStrategy, self).updateSlotAssignments(arg0)

    @overload
    def __init__(self, arg0: 'SlotCostProvider'):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>)"""
        val = _SoftRoleSlotAssignmentStrategy(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy as _BoundedSlotAssignmentStrategy
_BoundedSlotAssignmentStrategy = _BoundedSlotAssignmentStrategy
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy as _SoftRoleSlotAssignmentStrategy
_SoftRoleSlotAssignmentStrategy = _SoftRoleSlotAssignmentStrategy
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SoftRoleSlotAssignmentStrategy():
    """com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy"""
 
    @staticmethod
    def _wrap(java_value: _SoftRoleSlotAssignmentStrategy) -> 'SoftRoleSlotAssignmentStrategy':
        return SoftRoleSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SoftRoleSlotAssignmentStrategy):
        """
        Dynamic initializer for SoftRoleSlotAssignmentStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SoftRoleSlotAssignmentStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SoftRoleSlotAssignmentStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(_BoundedSlotAssignmentStrategy, self).removeSlotAssignment(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'SlotCostProvider', arg1: float):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>,float)"""
        val = _SoftRoleSlotAssignmentStrategy(arg0, _float.valueOf(arg1))
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

    @overload
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int._wrap(super(_BoundedSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

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

    @override
    @overload
    def updateSlotAssignments(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        super(_SoftRoleSlotAssignmentStrategy, self).updateSlotAssignments(arg0)

    @overload
    def __init__(self, arg0: 'SlotCostProvider'):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>)"""
        val = _SoftRoleSlotAssignmentStrategy(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationMember
import com.badlogic.gdx.ai.fma.FormationMember as _FormationMember
_FormationMember = _FormationMember
from abc import abstractmethod, ABC
 
class FormationMember():
    """com.badlogic.gdx.ai.fma.FormationMember"""
 
    @staticmethod
    def _wrap(java_value: _FormationMember) -> 'FormationMember':
        return FormationMember(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormationMember):
        """
        Dynamic initializer for FormationMember.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormationMember__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormationMember__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getTargetLocation(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.FormationMember.getTargetLocation()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SlotAssignment
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.fma.SlotAssignment as _SlotAssignment
_SlotAssignment = _SlotAssignment
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SlotAssignment():
    """com.badlogic.gdx.ai.fma.SlotAssignment"""
 
    @staticmethod
    def _wrap(java_value: _SlotAssignment) -> 'SlotAssignment':
        return SlotAssignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SlotAssignment):
        """
        Dynamic initializer for SlotAssignment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SlotAssignment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SlotAssignment__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FormationMember'):
        """public com.badlogic.gdx.ai.fma.SlotAssignment(com.badlogic.gdx.ai.fma.FormationMember<T>)"""
        val = _SlotAssignment(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FormationMember', arg1: int):
        """public com.badlogic.gdx.ai.fma.SlotAssignment(com.badlogic.gdx.ai.fma.FormationMember<T>,int)"""
        val = _SlotAssignment(arg0, _int.valueOf(arg1))
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
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationMotionModerator
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
import com.badlogic.gdx.ai.fma.FormationMotionModerator as _FormationMotionModerator
_FormationMotionModerator = _FormationMotionModerator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormationMotionModerator():
    """com.badlogic.gdx.ai.fma.FormationMotionModerator"""
 
    @staticmethod
    def _wrap(java_value: _FormationMotionModerator) -> 'FormationMotionModerator':
        return FormationMotionModerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormationMotionModerator):
        """
        Dynamic initializer for FormationMotionModerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormationMotionModerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormationMotionModerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def calculateDriftOffset(self, arg0: 'Location', arg1: 'Array', arg2: 'FormationPattern') -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.FormationMotionModerator.calculateDriftOffset(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        return 'utils.Location'._wrap(super(_FormationMotionModerator, self).calculateDriftOffset(arg0, arg1, arg2))

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator()"""
        val = _FormationMotionModerator()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator()"""
        val = _FormationMotionModerator()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def updateAnchorPoint(self, arg0: 'Location'):
        """public abstract void com.badlogic.gdx.ai.fma.FormationMotionModerator.updateAnchorPoint(com.badlogic.gdx.ai.utils.Location<T>)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.ai.fma.Formation
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.fma.SlotAssignment as _SlotAssignment
_SlotAssignment = _SlotAssignment
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.fma.SlotAssignmentStrategy as _SlotAssignmentStrategy
_SlotAssignmentStrategy = _SlotAssignmentStrategy
import com.badlogic.gdx.ai.utils.Location as _Location
_Location = _Location
import java.lang.Integer as _int
import com.badlogic.gdx.ai.fma.Formation as _Formation
_Formation = _Formation
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
import com.badlogic.gdx.ai.fma.FormationPattern as _FormationPattern
_FormationPattern = _FormationPattern
import com.badlogic.gdx.ai.fma.FormationMotionModerator as _FormationMotionModerator
_FormationMotionModerator = _FormationMotionModerator
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Formation():
    """com.badlogic.gdx.ai.fma.Formation"""
 
    @staticmethod
    def _wrap(java_value: _Formation) -> 'Formation':
        return Formation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Formation):
        """
        Dynamic initializer for Formation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Formation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Formation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSlotAssignmentStrategy(self) -> 'SlotAssignmentStrategy':
        """public com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T> com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentStrategy()"""
        return 'SlotAssignmentStrategy'._wrap(super(Formation, self).getSlotAssignmentStrategy())

    @overload
    def getMotionModerator(self) -> 'FormationMotionModerator':
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator<T> com.badlogic.gdx.ai.fma.Formation.getMotionModerator()"""
        return 'FormationMotionModerator'._wrap(super(Formation, self).getMotionModerator())

    @overload
    def getPattern(self) -> 'FormationPattern':
        """public com.badlogic.gdx.ai.fma.FormationPattern<T> com.badlogic.gdx.ai.fma.Formation.getPattern()"""
        return 'FormationPattern'._wrap(super(Formation, self).getPattern())

    @overload
    def setPattern(self, arg0: 'FormationPattern'):
        """public void com.badlogic.gdx.ai.fma.Formation.setPattern(com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        super(_Formation, self).setPattern(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern', arg2: 'SlotAssignmentStrategy', arg3: 'FormationMotionModerator'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>,com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>,com.badlogic.gdx.ai.fma.FormationMotionModerator<T>)"""
        val = _Formation(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @overload
    def removeMember(self, arg0: 'FormationMember'):
        """public void com.badlogic.gdx.ai.fma.Formation.removeMember(com.badlogic.gdx.ai.fma.FormationMember<T>)"""
        super(_Formation, self).removeMember(arg0)

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        val = _Formation(arg0, arg1)
        self.__wrapper = val

    @overload
    def setMotionModerator(self, arg0: 'FormationMotionModerator'):
        """public void com.badlogic.gdx.ai.fma.Formation.setMotionModerator(com.badlogic.gdx.ai.fma.FormationMotionModerator<T>)"""
        super(_Formation, self).setMotionModerator(arg0)

    @overload
    def getSlotAssignmentCount(self) -> int:
        """public int com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentCount()"""
        return int._wrap(super(Formation, self).getSlotAssignmentCount())

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
    def updateSlots(self):
        """public void com.badlogic.gdx.ai.fma.Formation.updateSlots()"""
        super(Formation, self).updateSlots()

    @overload
    def getAnchorPoint(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.Formation.getAnchorPoint()"""
        return 'utils.Location'._wrap(super(Formation, self).getAnchorPoint())

    @overload
    def setAnchorPoint(self, arg0: 'Location'):
        """public void com.badlogic.gdx.ai.fma.Formation.setAnchorPoint(com.badlogic.gdx.ai.utils.Location<T>)"""
        super(_Formation, self).setAnchorPoint(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def changePattern(self, arg0: 'FormationPattern') -> bool:
        """public boolean com.badlogic.gdx.ai.fma.Formation.changePattern(com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        return bool._wrap(super(_Formation, self).changePattern(arg0))

    @overload
    def addMember(self, arg0: 'FormationMember') -> bool:
        """public boolean com.badlogic.gdx.ai.fma.Formation.addMember(com.badlogic.gdx.ai.fma.FormationMember<T>)"""
        return bool._wrap(super(_Formation, self).addMember(arg0))

    @overload
    def updateSlotAssignments(self):
        """public void com.badlogic.gdx.ai.fma.Formation.updateSlotAssignments()"""
        super(Formation, self).updateSlotAssignments()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern', arg2: 'SlotAssignmentStrategy'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>,com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>)"""
        val = _Formation(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getSlotAssignmentAt(self, arg0: int) -> 'SlotAssignment':
        """public com.badlogic.gdx.ai.fma.SlotAssignment<T> com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentAt(int)"""
        return 'SlotAssignment'._wrap(super(_Formation, self).getSlotAssignmentAt(_int.valueOf(arg0)))

    @overload
    def setSlotAssignmentStrategy(self, arg0: 'SlotAssignmentStrategy'):
        """public void com.badlogic.gdx.ai.fma.Formation.setSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>)"""
        super(_Formation, self).setSlotAssignmentStrategy(arg0)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationPattern
from pyquantum_helper import import_once as _import_once
from abc import abstractmethod, ABC
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import com.badlogic.gdx.ai.fma.FormationPattern as _FormationPattern
_FormationPattern = _FormationPattern
 
class FormationPattern():
    """com.badlogic.gdx.ai.fma.FormationPattern"""
 
    @staticmethod
    def _wrap(java_value: _FormationPattern) -> 'FormationPattern':
        return FormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormationPattern):
        """
        Dynamic initializer for FormationPattern.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormationPattern__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormationPattern__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def supportsSlots(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.ai.fma.FormationPattern.supportsSlots(int)"""
        pass

    @abstractmethod
    def setNumberOfSlots(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.fma.FormationPattern.setNumberOfSlots(int)"""
        pass

    @abstractmethod
    def calculateSlotLocation(self, arg0: 'Location', arg1: int):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.FormationPattern.calculateSlotLocation(com.badlogic.gdx.ai.utils.Location<T>,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider
import com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy as _SoftRoleSlotAssignmentStrategy_SlotCostProvider
_SlotCostProvider = _SoftRoleSlotAssignmentStrategy_SlotCostProvider.SlotCostProvider
from abc import abstractmethod, ABC
 
class SlotCostProvider():
    """com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy.SlotCostProvider"""
 
    @staticmethod
    def _wrap(java_value: _SlotCostProvider) -> 'SlotCostProvider':
        return SlotCostProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SlotCostProvider):
        """
        Dynamic initializer for SlotCostProvider.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SlotCostProvider__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SlotCostProvider__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getCost(self, arg0: 'FormationMember', arg1: int):
        """public abstract float com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider.getCost(com.badlogic.gdx.ai.fma.FormationMember<T>,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SlotAssignmentStrategy
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.fma.SlotAssignmentStrategy as _SlotAssignmentStrategy
_SlotAssignmentStrategy = _SlotAssignmentStrategy
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from abc import abstractmethod, ABC
 
class SlotAssignmentStrategy():
    """com.badlogic.gdx.ai.fma.SlotAssignmentStrategy"""
 
    @staticmethod
    def _wrap(java_value: _SlotAssignmentStrategy) -> 'SlotAssignmentStrategy':
        return SlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SlotAssignmentStrategy):
        """
        Dynamic initializer for SlotAssignmentStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SlotAssignmentStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SlotAssignmentStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def calculateNumberOfSlots(self, arg0: 'Array'):
        """public abstract int com.badlogic.gdx.ai.fma.SlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        pass

    @abstractmethod
    def updateSlotAssignments(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.ai.fma.SlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        pass

    @abstractmethod
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public abstract void com.badlogic.gdx.ai.fma.SlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy as _BoundedSlotAssignmentStrategy
_BoundedSlotAssignmentStrategy = _BoundedSlotAssignmentStrategy
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoundedSlotAssignmentStrategy():
    """com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy"""
 
    @staticmethod
    def _wrap(java_value: _BoundedSlotAssignmentStrategy) -> 'BoundedSlotAssignmentStrategy':
        return BoundedSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundedSlotAssignmentStrategy):
        """
        Dynamic initializer for BoundedSlotAssignmentStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundedSlotAssignmentStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundedSlotAssignmentStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy()"""
        val = _BoundedSlotAssignmentStrategy()
        self.__wrapper = val

    @abstractmethod
    def updateSlotAssignments(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy()"""
        val = _BoundedSlotAssignmentStrategy()
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
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(_BoundedSlotAssignmentStrategy, self).removeSlotAssignment(arg0, _int.valueOf(arg1))

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
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int._wrap(super(_BoundedSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy as _FreeSlotAssignmentStrategy
_FreeSlotAssignmentStrategy = _FreeSlotAssignmentStrategy
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FreeSlotAssignmentStrategy():
    """com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy"""
 
    @staticmethod
    def _wrap(java_value: _FreeSlotAssignmentStrategy) -> 'FreeSlotAssignmentStrategy':
        return FreeSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FreeSlotAssignmentStrategy):
        """
        Dynamic initializer for FreeSlotAssignmentStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FreeSlotAssignmentStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FreeSlotAssignmentStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy()"""
        val = _FreeSlotAssignmentStrategy()
        self.__wrapper = val

    @overload
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int._wrap(super(_FreeSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

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
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(_FreeSlotAssignmentStrategy, self).removeSlotAssignment(arg0, _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def updateSlotAssignments(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        super(_FreeSlotAssignmentStrategy, self).updateSlotAssignments(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy()"""
        val = _FreeSlotAssignmentStrategy()
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