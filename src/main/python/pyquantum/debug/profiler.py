from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.debug.profiler.ProfileData as __ProfileData
__ProfileData = __ProfileData
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Profiler(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.debug.profiler.Profiler"""
 
    @staticmethod
    def __wrap(java_value: __Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Profiler):
        """
        Dynamic initializer for Profiler.
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
    def update(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.update()"""
        super(Profiler, self).update()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(__Profiler, self).section(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = __Profiler()
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

    @overload
    def setProfiling(self, arg0: bool):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.setProfiling(boolean)"""
        super(__Profiler, self).setProfiling(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = __Profiler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isProfiling(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Profiler.isProfiling()"""
        return bool.__wrap(super(Profiler, self).isProfiling())

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
    def collect(self) -> 'ProfileData':
        """public dev.ultreon.quantum.debug.profiler.ProfileData dev.ultreon.quantum.debug.profiler.Profiler.collect()"""
        return 'ProfileData'.__wrap(super(Profiler, self).collect())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.dispose()"""
        super(Profiler, self).dispose()

 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Profiler
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.debug.profiler.ProfileData as __ProfileData
__ProfileData = __ProfileData
from builtins import type
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Profiler(pygdx.__Disposable, utils.Disposable):
    """dev.ultreon.quantum.debug.profiler.Profiler"""
 
    @staticmethod
    def __wrap(java_value: __Profiler) -> 'Profiler':
        return Profiler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Profiler):
        """
        Dynamic initializer for Profiler.
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
    def update(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.update()"""
        super(Profiler, self).update()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def section(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.section(java.lang.String,java.lang.Runnable)"""
        super(__Profiler, self).section(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = __Profiler()
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

    @overload
    def setProfiling(self, arg0: bool):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.setProfiling(boolean)"""
        super(__Profiler, self).setProfiling(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.profiler.Profiler()"""
        val = __Profiler()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isProfiling(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Profiler.isProfiling()"""
        return bool.__wrap(super(Profiler, self).isProfiling())

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
    def collect(self) -> 'ProfileData':
        """public dev.ultreon.quantum.debug.profiler.ProfileData dev.ultreon.quantum.debug.profiler.Profiler.collect()"""
        return 'ProfileData'.__wrap(super(Profiler, self).collect())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void dev.ultreon.quantum.debug.profiler.Profiler.dispose()"""
        super(Profiler, self).dispose()

 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Profiler 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ProfileData
import java.lang.Thread as Thread
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.debug.profiler.Section as __Section_FinishedSection
__FinishedSection = __Section_FinishedSection.FinishedSection
import java.lang.Object as __object
import dev.ultreon.quantum.debug.profiler.ProfileData as __ProfileData
__ProfileData = __ProfileData
from builtins import type
import java.util.Set as __Set
__Set = __Set
import dev.ultreon.quantum.debug.profiler.ThreadSection as __ThreadSection_FinishedThreadSection
__FinishedThreadSection = __ThreadSection_FinishedThreadSection.FinishedThreadSection
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class ProfileData():
    """dev.ultreon.quantum.debug.profiler.ProfileData"""
 
    @staticmethod
    def __wrap(java_value: __ProfileData) -> 'ProfileData':
        return ProfileData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProfileData):
        """
        Dynamic initializer for ProfileData.
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
    def getThreads(self) -> 'Set':
        """public java.util.Set<java.lang.Thread> dev.ultreon.quantum.debug.profiler.ProfileData.getThreads()"""
        return 'Set'.__wrap(super(ProfileData, self).getThreads())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getSection(self, arg0: 'FinishedThreadSection', arg1: str) -> 'FinishedSection':
        """public dev.ultreon.quantum.debug.profiler.Section$FinishedSection dev.ultreon.quantum.debug.profiler.ProfileData.getSection(dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection,java.lang.String)"""
        return 'FinishedSection'.__wrap(super(__ProfileData, self).getSection(arg0, arg1))

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
    def __init__(self, arg0: 'Map'):
        """public dev.ultreon.quantum.debug.profiler.ProfileData(java.util.Map<java.lang.Thread, dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection>)"""
        val = __ProfileData(arg0)
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
    def getThreadSection(self, arg0: 'Thread') -> 'FinishedThreadSection':
        """public dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection dev.ultreon.quantum.debug.profiler.ProfileData.getThreadSection(java.lang.Thread)"""
        return 'FinishedThreadSection'.__wrap(super(__ProfileData, self).getThreadSection(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Section
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.debug.profiler.Section as __Section
__Section = __Section
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class Section():
    """dev.ultreon.quantum.debug.profiler.Section"""
 
    @staticmethod
    def __wrap(java_value: __Section) -> 'Section':
        return Section(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Section):
        """
        Dynamic initializer for Section.
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
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section.toString()"""
        return str.__wrap(super(Section, self).toString())

    @overload
    def getEnd(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getEnd()"""
        return int.__wrap(super(Section, self).getEnd())

    @overload
    def getNanos(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getNanos()"""
        return int.__wrap(super(Section, self).getNanos())

    @overload
    def getStart(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section.getStart()"""
        return int.__wrap(super(Section, self).getStart())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section.getName()"""
        return str.__wrap(super(Section, self).getName())

    @overload
    def collect(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.Section.collect()"""
        return 'Map'.__wrap(super(Section, self).collect())

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
    def __init__(self, arg0: str, arg1: 'Profiler'):
        """public dev.ultreon.quantum.debug.profiler.Section(java.lang.String,dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = __Section(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def hasCurrent(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.profiler.Section.hasCurrent()"""
        return bool.__wrap(super(Section, self).hasCurrent())

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
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section> dev.ultreon.quantum.debug.profiler.Section.getData()"""
        return 'Map'.__wrap(super(Section, self).getData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.debug.profiler.ThreadSection as __ThreadSection_FinishedThreadSection
__FinishedThreadSection = __ThreadSection_FinishedThreadSection.FinishedThreadSection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class FinishedThreadSection():
    """dev.ultreon.quantum.debug.profiler.ThreadSection.FinishedThreadSection"""
 
    @staticmethod
    def __wrap(java_value: __FinishedThreadSection) -> 'FinishedThreadSection':
        return FinishedThreadSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinishedThreadSection):
        """
        Dynamic initializer for FinishedThreadSection.
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

    @staticmethod
    @overload
    def create(arg0: 'ThreadSection') -> 'FinishedThreadSection':
        """public static dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection.create(dev.ultreon.quantum.debug.profiler.ThreadSection)"""
        return FinishedThreadSection.__wrap(__FinishedThreadSection.create(arg0))

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

    @overload
    def __init__(self, arg0: 'ThreadSection'):
        """public dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection(dev.ultreon.quantum.debug.profiler.ThreadSection)"""
        val = __FinishedThreadSection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.ThreadSection$FinishedThreadSection.getData()"""
        return 'Map'.__wrap(super(FinishedThreadSection, self).getData())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.ThreadSection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.debug.profiler.ThreadSection as __ThreadSection
__ThreadSection = __ThreadSection
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class ThreadSection():
    """dev.ultreon.quantum.debug.profiler.ThreadSection"""
 
    @staticmethod
    def __wrap(java_value: __ThreadSection) -> 'ThreadSection':
        return ThreadSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadSection):
        """
        Dynamic initializer for ThreadSection.
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

    @overload
    def __init__(self, arg0: 'Profiler'):
        """public dev.ultreon.quantum.debug.profiler.ThreadSection(dev.ultreon.quantum.debug.profiler.Profiler)"""
        val = __ThreadSection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section> dev.ultreon.quantum.debug.profiler.ThreadSection.getData()"""
        return 'Map'.__wrap(super(ThreadSection, self).getData())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.profiler.Section$FinishedSection
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.debug.profiler.Section as __Section_FinishedSection
__FinishedSection = __Section_FinishedSection.FinishedSection
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
from builtins import int
 
class FinishedSection():
    """dev.ultreon.quantum.debug.profiler.Section.FinishedSection"""
 
    @staticmethod
    def __wrap(java_value: __FinishedSection) -> 'FinishedSection':
        return FinishedSection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FinishedSection):
        """
        Dynamic initializer for FinishedSection.
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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getName()"""
        return str.__wrap(super(FinishedSection, self).getName())

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

    @overload
    def __init__(self, arg0: 'Section'):
        """public dev.ultreon.quantum.debug.profiler.Section$FinishedSection(dev.ultreon.quantum.debug.profiler.Section)"""
        val = __FinishedSection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.debug.profiler.Section$FinishedSection> dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getData()"""
        return 'Map'.__wrap(super(FinishedSection, self).getData())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getNanos(self) -> int:
        """public long dev.ultreon.quantum.debug.profiler.Section$FinishedSection.getNanos()"""
        return int.__wrap(super(FinishedSection, self).getNanos())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))