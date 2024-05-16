from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.fma.FormationPattern as __FormationPattern
__FormationPattern = __FormationPattern
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

 
class FormationPattern(ABC):
    """com.badlogic.gdx.ai.fma.FormationPattern"""
 
    @staticmethod
    def __wrap(java_value: __FormationPattern) -> 'FormationPattern':
        return FormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormationPattern):
        """
        Dynamic initializer for FormationPattern.
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationPattern
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.fma.FormationPattern as __FormationPattern
__FormationPattern = __FormationPattern
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

 
class FormationPattern(ABC):
    """com.badlogic.gdx.ai.fma.FormationPattern"""
 
    @staticmethod
    def __wrap(java_value: __FormationPattern) -> 'FormationPattern':
        return FormationPattern(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormationPattern):
        """
        Dynamic initializer for FormationPattern.
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

 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationPattern 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy as __FreeSlotAssignmentStrategy
__FreeSlotAssignmentStrategy = __FreeSlotAssignmentStrategy
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FreeSlotAssignmentStrategy(__SlotAssignmentStrategy, SlotAssignmentStrategy):
    """com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy"""
 
    @staticmethod
    def __wrap(java_value: __FreeSlotAssignmentStrategy) -> 'FreeSlotAssignmentStrategy':
        return FreeSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FreeSlotAssignmentStrategy):
        """
        Dynamic initializer for FreeSlotAssignmentStrategy.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy()"""
        val = __FreeSlotAssignmentStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(__FreeSlotAssignmentStrategy, self).removeSlotAssignment(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int.__wrap(super(__FreeSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy()"""
        val = __FreeSlotAssignmentStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def updateSlotAssignments(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.fma.FreeSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        super(__FreeSlotAssignmentStrategy, self).updateSlotAssignments(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy as __BoundedSlotAssignmentStrategy
__BoundedSlotAssignmentStrategy = __BoundedSlotAssignmentStrategy
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BoundedSlotAssignmentStrategy(ABC, __SlotAssignmentStrategy, SlotAssignmentStrategy):
    """com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy"""
 
    @staticmethod
    def __wrap(java_value: __BoundedSlotAssignmentStrategy) -> 'BoundedSlotAssignmentStrategy':
        return BoundedSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundedSlotAssignmentStrategy):
        """
        Dynamic initializer for BoundedSlotAssignmentStrategy.
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

    @abstractmethod
    def updateSlotAssignments(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(__BoundedSlotAssignmentStrategy, self).removeSlotAssignment(arg0, __int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy()"""
        val = __BoundedSlotAssignmentStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy()"""
        val = __BoundedSlotAssignmentStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int.__wrap(super(__BoundedSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SlotAssignmentStrategy
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.ai.fma.SlotAssignmentStrategy as __SlotAssignmentStrategy
__SlotAssignmentStrategy = __SlotAssignmentStrategy
from abc import abstractmethod, ABC
 
class SlotAssignmentStrategy(ABC):
    """com.badlogic.gdx.ai.fma.SlotAssignmentStrategy"""
 
    @staticmethod
    def __wrap(java_value: __SlotAssignmentStrategy) -> 'SlotAssignmentStrategy':
        return SlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SlotAssignmentStrategy):
        """
        Dynamic initializer for SlotAssignmentStrategy.
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
 
 
# CLASS: com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider
import com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy as __SoftRoleSlotAssignmentStrategy_SlotCostProvider
__SlotCostProvider = __SoftRoleSlotAssignmentStrategy_SlotCostProvider.SlotCostProvider
from abc import abstractmethod, ABC
 
class SlotCostProvider(ABC):
    """com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy.SlotCostProvider"""
 
    @staticmethod
    def __wrap(java_value: __SlotCostProvider) -> 'SlotCostProvider':
        return SlotCostProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SlotCostProvider):
        """
        Dynamic initializer for SlotCostProvider.
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
    def getCost(self, arg0: 'FormationMember', arg1: int):
        """public abstract float com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider.getCost(com.badlogic.gdx.ai.fma.FormationMember<T>,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationMotionModerator
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.fma.FormationMotionModerator as __FormationMotionModerator
__FormationMotionModerator = __FormationMotionModerator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
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
 
class FormationMotionModerator(ABC):
    """com.badlogic.gdx.ai.fma.FormationMotionModerator"""
 
    @staticmethod
    def __wrap(java_value: __FormationMotionModerator) -> 'FormationMotionModerator':
        return FormationMotionModerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormationMotionModerator):
        """
        Dynamic initializer for FormationMotionModerator.
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

    @overload
    def calculateDriftOffset(self, arg0: 'Location', arg1: 'Array', arg2: 'FormationPattern') -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.FormationMotionModerator.calculateDriftOffset(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        return 'utils.Location'.__wrap(super(__FormationMotionModerator, self).calculateDriftOffset(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator()"""
        val = __FormationMotionModerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator()"""
        val = __FormationMotionModerator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.Formation
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.fma.SlotAssignmentStrategy as __SlotAssignmentStrategy
__SlotAssignmentStrategy = __SlotAssignmentStrategy
import java.lang.Object as __object
import com.badlogic.gdx.ai.fma.Formation as __Formation
__Formation = __Formation
from builtins import type
import com.badlogic.gdx.ai.utils.Location as __Location
__Location = __Location
import com.badlogic.gdx.ai.fma.FormationMotionModerator as __FormationMotionModerator
__FormationMotionModerator = __FormationMotionModerator
import com.badlogic.gdx.ai.fma.SlotAssignment as __SlotAssignment
__SlotAssignment = __SlotAssignment
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.fma.FormationPattern as __FormationPattern
__FormationPattern = __FormationPattern
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class Formation():
    """com.badlogic.gdx.ai.fma.Formation"""
 
    @staticmethod
    def __wrap(java_value: __Formation) -> 'Formation':
        return Formation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Formation):
        """
        Dynamic initializer for Formation.
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
    def setSlotAssignmentStrategy(self, arg0: 'SlotAssignmentStrategy'):
        """public void com.badlogic.gdx.ai.fma.Formation.setSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>)"""
        super(__Formation, self).setSlotAssignmentStrategy(arg0)

    @overload
    def getSlotAssignmentStrategy(self) -> 'SlotAssignmentStrategy':
        """public com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T> com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentStrategy()"""
        return 'SlotAssignmentStrategy'.__wrap(super(Formation, self).getSlotAssignmentStrategy())

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern', arg2: 'SlotAssignmentStrategy'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>,com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>)"""
        val = __Formation(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        val = __Formation(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setMotionModerator(self, arg0: 'FormationMotionModerator'):
        """public void com.badlogic.gdx.ai.fma.Formation.setMotionModerator(com.badlogic.gdx.ai.fma.FormationMotionModerator<T>)"""
        super(__Formation, self).setMotionModerator(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def updateSlots(self):
        """public void com.badlogic.gdx.ai.fma.Formation.updateSlots()"""
        super(Formation, self).updateSlots()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Location', arg1: 'FormationPattern', arg2: 'SlotAssignmentStrategy', arg3: 'FormationMotionModerator'):
        """public com.badlogic.gdx.ai.fma.Formation(com.badlogic.gdx.ai.utils.Location<T>,com.badlogic.gdx.ai.fma.FormationPattern<T>,com.badlogic.gdx.ai.fma.SlotAssignmentStrategy<T>,com.badlogic.gdx.ai.fma.FormationMotionModerator<T>)"""
        val = __Formation(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeMember(self, arg0: 'FormationMember'):
        """public void com.badlogic.gdx.ai.fma.Formation.removeMember(com.badlogic.gdx.ai.fma.FormationMember<T>)"""
        super(__Formation, self).removeMember(arg0)

    @overload
    def getSlotAssignmentCount(self) -> int:
        """public int com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentCount()"""
        return int.__wrap(super(Formation, self).getSlotAssignmentCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addMember(self, arg0: 'FormationMember') -> bool:
        """public boolean com.badlogic.gdx.ai.fma.Formation.addMember(com.badlogic.gdx.ai.fma.FormationMember<T>)"""
        return bool.__wrap(super(__Formation, self).addMember(arg0))

    @overload
    def getSlotAssignmentAt(self, arg0: int) -> 'SlotAssignment':
        """public com.badlogic.gdx.ai.fma.SlotAssignment<T> com.badlogic.gdx.ai.fma.Formation.getSlotAssignmentAt(int)"""
        return 'SlotAssignment'.__wrap(super(__Formation, self).getSlotAssignmentAt(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def updateSlotAssignments(self):
        """public void com.badlogic.gdx.ai.fma.Formation.updateSlotAssignments()"""
        super(Formation, self).updateSlotAssignments()

    @overload
    def getMotionModerator(self) -> 'FormationMotionModerator':
        """public com.badlogic.gdx.ai.fma.FormationMotionModerator<T> com.badlogic.gdx.ai.fma.Formation.getMotionModerator()"""
        return 'FormationMotionModerator'.__wrap(super(Formation, self).getMotionModerator())

    @overload
    def getAnchorPoint(self) -> 'utils.Location':
        """public com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.Formation.getAnchorPoint()"""
        return 'utils.Location'.__wrap(super(Formation, self).getAnchorPoint())

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
    def changePattern(self, arg0: 'FormationPattern') -> bool:
        """public boolean com.badlogic.gdx.ai.fma.Formation.changePattern(com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        return bool.__wrap(super(__Formation, self).changePattern(arg0))

    @overload
    def getPattern(self) -> 'FormationPattern':
        """public com.badlogic.gdx.ai.fma.FormationPattern<T> com.badlogic.gdx.ai.fma.Formation.getPattern()"""
        return 'FormationPattern'.__wrap(super(Formation, self).getPattern())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPattern(self, arg0: 'FormationPattern'):
        """public void com.badlogic.gdx.ai.fma.Formation.setPattern(com.badlogic.gdx.ai.fma.FormationPattern<T>)"""
        super(__Formation, self).setPattern(arg0)

    @overload
    def setAnchorPoint(self, arg0: 'Location'):
        """public void com.badlogic.gdx.ai.fma.Formation.setAnchorPoint(com.badlogic.gdx.ai.utils.Location<T>)"""
        super(__Formation, self).setAnchorPoint(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.FormationMember
import com.badlogic.gdx.ai.fma.FormationMember as __FormationMember
__FormationMember = __FormationMember
from abc import abstractmethod, ABC
 
class FormationMember(ABC):
    """com.badlogic.gdx.ai.fma.FormationMember"""
 
    @staticmethod
    def __wrap(java_value: __FormationMember) -> 'FormationMember':
        return FormationMember(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormationMember):
        """
        Dynamic initializer for FormationMember.
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
    def getTargetLocation(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Location<T> com.badlogic.gdx.ai.fma.FormationMember.getTargetLocation()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy as __SoftRoleSlotAssignmentStrategy
__SoftRoleSlotAssignmentStrategy = __SoftRoleSlotAssignmentStrategy
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy as __BoundedSlotAssignmentStrategy
__BoundedSlotAssignmentStrategy = __BoundedSlotAssignmentStrategy
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SoftRoleSlotAssignmentStrategy(__BoundedSlotAssignmentStrategy, BoundedSlotAssignmentStrategy):
    """com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy"""
 
    @staticmethod
    def __wrap(java_value: __SoftRoleSlotAssignmentStrategy) -> 'SoftRoleSlotAssignmentStrategy':
        return SoftRoleSlotAssignmentStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SoftRoleSlotAssignmentStrategy):
        """
        Dynamic initializer for SoftRoleSlotAssignmentStrategy.
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
    def removeSlotAssignment(self, arg0: 'Array', arg1: int):
        """public void com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.removeSlotAssignment(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>,int)"""
        super(__BoundedSlotAssignmentStrategy, self).removeSlotAssignment(arg0, __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'SlotCostProvider'):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>)"""
        val = __SoftRoleSlotAssignmentStrategy(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def updateSlotAssignments(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy.updateSlotAssignments(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        super(__SoftRoleSlotAssignmentStrategy, self).updateSlotAssignments(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'SlotCostProvider', arg1: float):
        """public com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy(com.badlogic.gdx.ai.fma.SoftRoleSlotAssignmentStrategy$SlotCostProvider<T>,float)"""
        val = __SoftRoleSlotAssignmentStrategy(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def calculateNumberOfSlots(self, arg0: 'Array') -> int:
        """public int com.badlogic.gdx.ai.fma.BoundedSlotAssignmentStrategy.calculateNumberOfSlots(com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.fma.SlotAssignment<T>>)"""
        return int.__wrap(super(__BoundedSlotAssignmentStrategy, self).calculateNumberOfSlots(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.fma.SlotAssignment
import com.badlogic.gdx.ai.fma.SlotAssignment as __SlotAssignment
__SlotAssignment = __SlotAssignment
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SlotAssignment():
    """com.badlogic.gdx.ai.fma.SlotAssignment"""
 
    @staticmethod
    def __wrap(java_value: __SlotAssignment) -> 'SlotAssignment':
        return SlotAssignment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SlotAssignment):
        """
        Dynamic initializer for SlotAssignment.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'FormationMember', arg1: int):
        """public com.badlogic.gdx.ai.fma.SlotAssignment(com.badlogic.gdx.ai.fma.FormationMember<T>,int)"""
        val = __SlotAssignment(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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
        val = __SlotAssignment(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))