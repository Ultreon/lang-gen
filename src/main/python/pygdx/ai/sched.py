from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.sched.LoadBalancingScheduler as _LoadBalancingScheduler
_LoadBalancingScheduler = _LoadBalancingScheduler
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoadBalancingScheduler():
    """com.badlogic.gdx.ai.sched.LoadBalancingScheduler"""
 
    @staticmethod
    def _wrap(java_value: _LoadBalancingScheduler) -> 'LoadBalancingScheduler':
        return LoadBalancingScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadBalancingScheduler):
        """
        Dynamic initializer for LoadBalancingScheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadBalancingScheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadBalancingScheduler__wrapper":
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
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(_LoadBalancingScheduler, self).add(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.LoadBalancingScheduler(int)"""
        val = _LoadBalancingScheduler(_int.valueOf(arg0))
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
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.run(long)"""
        super(_LoadBalancingScheduler, self).run(_long.valueOf(arg0))

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
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(_LoadBalancingScheduler, self).addWithAutomaticPhasing(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.sched.LoadBalancingScheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.sched.LoadBalancingScheduler as _LoadBalancingScheduler
_LoadBalancingScheduler = _LoadBalancingScheduler
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoadBalancingScheduler():
    """com.badlogic.gdx.ai.sched.LoadBalancingScheduler"""
 
    @staticmethod
    def _wrap(java_value: _LoadBalancingScheduler) -> 'LoadBalancingScheduler':
        return LoadBalancingScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoadBalancingScheduler):
        """
        Dynamic initializer for LoadBalancingScheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoadBalancingScheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoadBalancingScheduler__wrapper":
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
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(_LoadBalancingScheduler, self).add(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.LoadBalancingScheduler(int)"""
        val = _LoadBalancingScheduler(_int.valueOf(arg0))
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
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.run(long)"""
        super(_LoadBalancingScheduler, self).run(_long.valueOf(arg0))

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
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.LoadBalancingScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(_LoadBalancingScheduler, self).addWithAutomaticPhasing(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.sched.LoadBalancingScheduler 
 
 
# CLASS: com.badlogic.gdx.ai.sched.PriorityScheduler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.sched.PriorityScheduler as _PriorityScheduler
_PriorityScheduler = _PriorityScheduler
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PriorityScheduler():
    """com.badlogic.gdx.ai.sched.PriorityScheduler"""
 
    @staticmethod
    def _wrap(java_value: _PriorityScheduler) -> 'PriorityScheduler':
        return PriorityScheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PriorityScheduler):
        """
        Dynamic initializer for PriorityScheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PriorityScheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PriorityScheduler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.run(long)"""
        super(_PriorityScheduler, self).run(_long.valueOf(arg0))

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
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        super(_PriorityScheduler, self).add(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int, arg3: float):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int,float)"""
        super(_PriorityScheduler, self).add(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

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
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        super(_PriorityScheduler, self).addWithAutomaticPhasing(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.PriorityScheduler(int)"""
        val = _PriorityScheduler(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int, arg2: float):
        """public void com.badlogic.gdx.ai.sched.PriorityScheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int,float)"""
        super(_PriorityScheduler, self).addWithAutomaticPhasing(arg0, _int.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.sched.Schedulable
import com.badlogic.gdx.ai.sched.Schedulable as _Schedulable
_Schedulable = _Schedulable
from abc import abstractmethod, ABC
 
class Schedulable():
    """com.badlogic.gdx.ai.sched.Schedulable"""
 
    @staticmethod
    def _wrap(java_value: _Schedulable) -> 'Schedulable':
        return Schedulable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Schedulable):
        """
        Dynamic initializer for Schedulable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Schedulable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Schedulable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.sched.SchedulerBase$SchedulableRecord
import com.badlogic.gdx.ai.sched.SchedulerBase as _SchedulerBase_SchedulableRecord
_SchedulableRecord = _SchedulerBase_SchedulableRecord.SchedulableRecord
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SchedulableRecord():
    """com.badlogic.gdx.ai.sched.SchedulerBase.SchedulableRecord"""
 
    @staticmethod
    def _wrap(java_value: _SchedulableRecord) -> 'SchedulableRecord':
        return SchedulableRecord(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SchedulableRecord):
        """
        Dynamic initializer for SchedulableRecord.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SchedulableRecord__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SchedulableRecord__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.sched.SchedulerBase
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.sched.Scheduler as _Scheduler
_Scheduler = _Scheduler
import com.badlogic.gdx.ai.sched.Schedulable as _Schedulable
_Schedulable = _Schedulable
import java.lang.Integer as _int
import com.badlogic.gdx.ai.sched.SchedulerBase as _SchedulerBase
_SchedulerBase = _SchedulerBase
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SchedulerBase():
    """com.badlogic.gdx.ai.sched.SchedulerBase"""
 
    @staticmethod
    def _wrap(java_value: _SchedulerBase) -> 'SchedulerBase':
        return SchedulerBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SchedulerBase):
        """
        Dynamic initializer for SchedulerBase.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SchedulerBase__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SchedulerBase__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass

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

    @abstractmethod
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.sched.SchedulerBase(int)"""
        val = _SchedulerBase(_int.valueOf(arg0))
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

    @abstractmethod
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.sched.Scheduler
import com.badlogic.gdx.ai.sched.Scheduler as _Scheduler
_Scheduler = _Scheduler
import com.badlogic.gdx.ai.sched.Schedulable as _Schedulable
_Schedulable = _Schedulable
from abc import abstractmethod, ABC
 
class Scheduler():
    """com.badlogic.gdx.ai.sched.Scheduler"""
 
    @staticmethod
    def _wrap(java_value: _Scheduler) -> 'Scheduler':
        return Scheduler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Scheduler):
        """
        Dynamic initializer for Scheduler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Scheduler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Scheduler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.sched.Schedulable.run(long)"""
        pass

    @abstractmethod
    def addWithAutomaticPhasing(self, arg0: 'Schedulable', arg1: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.addWithAutomaticPhasing(com.badlogic.gdx.ai.sched.Schedulable,int)"""
        pass

    @abstractmethod
    def add(self, arg0: 'Schedulable', arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.ai.sched.Scheduler.add(com.badlogic.gdx.ai.sched.Schedulable,int,int)"""
        pass