from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.util.PropertiesPropertySource as __PropertiesPropertySource
__PropertiesPropertySource = __PropertiesPropertySource
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PropertiesPropertySource():
    """org.apache.logging.log4j.util.PropertiesPropertySource"""
 
    @staticmethod
    def __wrap(java_value: __PropertiesPropertySource) -> 'PropertiesPropertySource':
        return PropertiesPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertiesPropertySource):
        """
        Dynamic initializer for PropertiesPropertySource.
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
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.PropertiesPropertySource.getPriority()"""
        return int.__wrap(super(PropertiesPropertySource, self).getPriority())

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.PropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__PropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, properties: 'Properties'):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties)"""
        val = __PropertiesPropertySource(properties)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesPropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__PropertiesPropertySource, self).getProperty(key))

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.PropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__PropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertiesPropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(PropertiesPropertySource, self).getPropertyNames())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertiesPropertySource, self).containsProperty(key))

    @overload
    def __init__(self, properties: 'Properties', priority: int):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties,int)"""
        val = __PropertiesPropertySource(properties, __int.valueOf(priority))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.util.PropertiesPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.util.PropertiesPropertySource as __PropertiesPropertySource
__PropertiesPropertySource = __PropertiesPropertySource
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PropertiesPropertySource():
    """org.apache.logging.log4j.util.PropertiesPropertySource"""
 
    @staticmethod
    def __wrap(java_value: __PropertiesPropertySource) -> 'PropertiesPropertySource':
        return PropertiesPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertiesPropertySource):
        """
        Dynamic initializer for PropertiesPropertySource.
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
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.PropertiesPropertySource.getPriority()"""
        return int.__wrap(super(PropertiesPropertySource, self).getPriority())

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.PropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__PropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, properties: 'Properties'):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties)"""
        val = __PropertiesPropertySource(properties)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesPropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__PropertiesPropertySource, self).getProperty(key))

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.PropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__PropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertiesPropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(PropertiesPropertySource, self).getPropertyNames())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertiesPropertySource, self).containsProperty(key))

    @overload
    def __init__(self, properties: 'Properties', priority: int):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties,int)"""
        val = __PropertiesPropertySource(properties, __int.valueOf(priority))
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.logging.log4j.util.PropertiesPropertySource 
 
 
# CLASS: org.apache.logging.log4j.util.SystemPropertiesPropertySource
import org.apache.logging.log4j.util.SystemPropertiesPropertySource as __SystemPropertiesPropertySource
__SystemPropertiesPropertySource = __SystemPropertiesPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SystemPropertiesPropertySource():
    """org.apache.logging.log4j.util.SystemPropertiesPropertySource"""
 
    @staticmethod
    def __wrap(java_value: __SystemPropertiesPropertySource) -> 'SystemPropertiesPropertySource':
        return SystemPropertiesPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SystemPropertiesPropertySource):
        """
        Dynamic initializer for SystemPropertiesPropertySource.
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
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.SystemPropertiesPropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(SystemPropertiesPropertySource, self).getPropertyNames())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.SystemPropertiesPropertySource.getPriority()"""
        return int.__wrap(super(SystemPropertiesPropertySource, self).getPriority())

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.SystemPropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__SystemPropertiesPropertySource, self).containsProperty(key))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.SystemPropertiesPropertySource()"""
        val = __SystemPropertiesPropertySource()
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

    @staticmethod
    @overload
    def getSystemProperty(key: str, defaultValue: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.SystemPropertiesPropertySource.getSystemProperty(java.lang.String,java.lang.String)"""
        return str.__wrap(__SystemPropertiesPropertySource.getSystemProperty(key, defaultValue))

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.SystemPropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__SystemPropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.SystemPropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__SystemPropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.SystemPropertiesPropertySource()"""
        val = __SystemPropertiesPropertySource()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SystemPropertiesPropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__SystemPropertiesPropertySource, self).getProperty(key)) 
 
 
# CLASS: org.apache.logging.log4j.util.Timer$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.util.Timer as __Timer_Status
__Status = __Timer_Status.Status
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Status():
    """org.apache.logging.log4j.util.Timer.Status"""
 
    @staticmethod
    def __wrap(java_value: __Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Status):
        """
        Dynamic initializer for Status.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Status':
        """public static org.apache.logging.log4j.util.Timer$Status org.apache.logging.log4j.util.Timer$Status.valueOf(java.lang.String)"""
        return Status.__wrap(__Status.valueOf(name))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['Status']:
        """public static org.apache.logging.log4j.util.Timer$Status[] org.apache.logging.log4j.util.Timer$Status.values()"""
        return List[Status].__wrap(__Status.values()) 
 
 
# CLASS: org.apache.logging.log4j.util.ProcessIdUtil
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
import org.apache.logging.log4j.util.ProcessIdUtil as __ProcessIdUtil
__ProcessIdUtil = __ProcessIdUtil
from builtins import bool
from builtins import int
 
class ProcessIdUtil():
    """org.apache.logging.log4j.util.ProcessIdUtil"""
 
    @staticmethod
    def __wrap(java_value: __ProcessIdUtil) -> 'ProcessIdUtil':
        return ProcessIdUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProcessIdUtil):
        """
        Dynamic initializer for ProcessIdUtil.
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
    def __init__(self):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = __ProcessIdUtil()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = __ProcessIdUtil()
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

    @staticmethod
    @overload
    def getProcessId() -> str:
        """public static java.lang.String org.apache.logging.log4j.util.ProcessIdUtil.getProcessId()"""
        return str.__wrap(__ProcessIdUtil.getProcessId()) 
 
 
# CLASS: org.apache.logging.log4j.util.Constants
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import org.apache.logging.log4j.util.Constants as __Constants
__Constants = __Constants
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Constants():
    """org.apache.logging.log4j.util.Constants"""
 
    @staticmethod
    def __wrap(java_value: __Constants) -> 'Constants':
        return Constants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Constants):
        """
        Dynamic initializer for Constants.
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
 
 
# CLASS: org.apache.logging.log4j.util.LambdaUtil
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.apache.logging.log4j.util.LambdaUtil as __LambdaUtil
__LambdaUtil = __LambdaUtil
import java.lang.Object as __object
from builtins import type
try:
    from log4py import message
except ImportError:
    message = __import_once__("log4py.message")

from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
from typing import List
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
 
class LambdaUtil():
    """org.apache.logging.log4j.util.LambdaUtil"""
 
    @staticmethod
    def __wrap(java_value: __LambdaUtil) -> 'LambdaUtil':
        return LambdaUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LambdaUtil):
        """
        Dynamic initializer for LambdaUtil.
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

    @staticmethod
    @overload
    def getMessage(supplier: 'Supplier', messageFactory: 'MessageFactory') -> 'message.Message':
        """public static org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.LambdaUtil.getMessage(org.apache.logging.log4j.util.Supplier<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return message.Message.__wrap(__LambdaUtil.getMessage(supplier, messageFactory))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getAll(*suppliers: 'Supplier') -> List[object]:
        """public static java.lang.Object[] org.apache.logging.log4j.util.LambdaUtil.getAll(org.apache.logging.log4j.util.Supplier<?>...)"""
        return List[object].__wrap(__LambdaUtil.getAll(suppliers))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get(supplier: 'Supplier') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.LambdaUtil.get(org.apache.logging.log4j.util.Supplier<?>)"""
        return object.__wrap(__LambdaUtil.get(supplier))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(supplier: 'MessageSupplier') -> 'message.Message':
        """public static org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.LambdaUtil.get(org.apache.logging.log4j.util.MessageSupplier)"""
        return message.Message.__wrap(__LambdaUtil.get(supplier))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.PropertyFilePropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.util.PropertiesPropertySource as __PropertiesPropertySource
__PropertiesPropertySource = __PropertiesPropertySource
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import org.apache.logging.log4j.util.PropertyFilePropertySource as __PropertyFilePropertySource
__PropertyFilePropertySource = __PropertyFilePropertySource
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PropertyFilePropertySource():
    """org.apache.logging.log4j.util.PropertyFilePropertySource"""
 
    @staticmethod
    def __wrap(java_value: __PropertyFilePropertySource) -> 'PropertyFilePropertySource':
        return PropertyFilePropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertyFilePropertySource):
        """
        Dynamic initializer for PropertyFilePropertySource.
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
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.PropertiesPropertySource.getPriority()"""
        return int.__wrap(super(PropertiesPropertySource, self).getPriority())

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.PropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__PropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, fileName: str, useTccl: bool):
        """public org.apache.logging.log4j.util.PropertyFilePropertySource(java.lang.String,boolean)"""
        val = __PropertyFilePropertySource(fileName, __boolean.valueOf(useTccl))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesPropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__PropertiesPropertySource, self).getProperty(key))

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.PropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__PropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertiesPropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(PropertiesPropertySource, self).getPropertyNames())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertiesPropertySource, self).containsProperty(key))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, fileName: str):
        """public org.apache.logging.log4j.util.PropertyFilePropertySource(java.lang.String)"""
        val = __PropertyFilePropertySource(fileName)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.LazyBoolean
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.util.LazyBoolean as __LazyBoolean
__LazyBoolean = __LazyBoolean
import java.util.function.BooleanSupplier as BooleanSupplier
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
 
class LazyBoolean():
    """org.apache.logging.log4j.util.LazyBoolean"""
 
    @staticmethod
    def __wrap(java_value: __LazyBoolean) -> 'LazyBoolean':
        return LazyBoolean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LazyBoolean):
        """
        Dynamic initializer for LazyBoolean.
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
    def setAsBoolean(self, b: bool):
        """public void org.apache.logging.log4j.util.LazyBoolean.setAsBoolean(boolean)"""
        super(__LazyBoolean, self).setAsBoolean(__boolean.valueOf(b))

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
    def __init__(self, supplier: 'BooleanSupplier'):
        """public org.apache.logging.log4j.util.LazyBoolean(java.util.function.BooleanSupplier)"""
        val = __LazyBoolean(supplier)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self):
        """public void org.apache.logging.log4j.util.LazyBoolean.reset()"""
        super(LazyBoolean, self).reset()

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
    def getAsBoolean(self) -> bool:
        """public boolean org.apache.logging.log4j.util.LazyBoolean.getAsBoolean()"""
        return bool.__wrap(super(LazyBoolean, self).getAsBoolean())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.PropertiesUtil
from pyquantum_helper import transform as __transform
import java.lang.Boolean as __boolean
import java.lang.Long as Long
import java.nio.charset.Charset as Charset
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Double as __double
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
import java.nio.charset.Charset as __Charset
__Charset = __Charset
from builtins import float
import java.time.Duration as Duration
import org.apache.logging.log4j.util.PropertiesUtil as __PropertiesUtil
__PropertiesUtil = __PropertiesUtil
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.time.Duration as __Duration
__Duration = __Duration
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class PropertiesUtil():
    """org.apache.logging.log4j.util.PropertiesUtil"""
 
    @staticmethod
    def __wrap(java_value: __PropertiesUtil) -> 'PropertiesUtil':
        return PropertiesUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertiesUtil):
        """
        Dynamic initializer for PropertiesUtil.
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
    def getBooleanProperty(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertiesUtil, self).getBooleanProperty(name))

    @overload
    def getBooleanProperty(self, name: str, defaultValue: bool) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String,boolean)"""
        return bool.__wrap(super(__PropertiesUtil, self).getBooleanProperty(name, __boolean.valueOf(defaultValue)))

    @overload
    def getStringProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.String>)"""
        return str.__wrap(super(__PropertiesUtil, self).getStringProperty(prefixes, key, supplier))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasProperty(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.hasProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertiesUtil, self).hasProperty(name))

    @overload
    def __init__(self, propertiesFileName: str):
        """public org.apache.logging.log4j.util.PropertiesUtil(java.lang.String)"""
        val = __PropertiesUtil(propertiesFileName)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBooleanProperty(self, name: str, defaultValueIfAbsent: bool, defaultValueIfPresent: bool) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String,boolean,boolean)"""
        return bool.__wrap(super(__PropertiesUtil, self).getBooleanProperty(name, __boolean.valueOf(defaultValueIfAbsent), __boolean.valueOf(defaultValueIfPresent)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, props: 'Properties'):
        """public org.apache.logging.log4j.util.PropertiesUtil(java.util.Properties)"""
        val = __PropertiesUtil(props)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def extractSubset(properties: 'Properties', prefix: str) -> 'Properties':
        """public static java.util.Properties org.apache.logging.log4j.util.PropertiesUtil.extractSubset(java.util.Properties,java.lang.String)"""
        return Properties.__wrap(__PropertiesUtil.extractSubset(properties, prefix))

    @overload
    def getDoubleProperty(self, name: str, defaultValue: float) -> float:
        """public double org.apache.logging.log4j.util.PropertiesUtil.getDoubleProperty(java.lang.String,double)"""
        return float.__wrap(super(__PropertiesUtil, self).getDoubleProperty(name, __double.valueOf(defaultValue)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getIntegerProperty(self, name: str, defaultValue: int) -> int:
        """public int org.apache.logging.log4j.util.PropertiesUtil.getIntegerProperty(java.lang.String,int)"""
        return int.__wrap(super(__PropertiesUtil, self).getIntegerProperty(name, __int.valueOf(defaultValue)))

    @overload
    def getStringProperty(self, name: str, defaultValue: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__PropertiesUtil, self).getStringProperty(name, defaultValue))

    @overload
    def getDurationProperty(self, name: str, defaultValue: 'Duration') -> 'Duration':
        """public java.time.Duration org.apache.logging.log4j.util.PropertiesUtil.getDurationProperty(java.lang.String,java.time.Duration)"""
        return 'Duration'.__wrap(super(__PropertiesUtil, self).getDurationProperty(name, defaultValue))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLongProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Long':
        """public java.lang.Long org.apache.logging.log4j.util.PropertiesUtil.getLongProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Long>)"""
        return __transform(super(__PropertiesUtil, self).getLongProperty(prefixes, key, supplier)).'Long'Value()

    @overload
    def getStringProperty(self, name: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String)"""
        return str.__wrap(super(__PropertiesUtil, self).getStringProperty(name))

    @overload
    def getLongProperty(self, name: str, defaultValue: int) -> int:
        """public long org.apache.logging.log4j.util.PropertiesUtil.getLongProperty(java.lang.String,long)"""
        return int.__wrap(super(__PropertiesUtil, self).getLongProperty(name, __long.valueOf(defaultValue)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getCharsetProperty(self, name: str) -> 'Charset':
        """public java.nio.charset.Charset org.apache.logging.log4j.util.PropertiesUtil.getCharsetProperty(java.lang.String)"""
        return 'Charset'.__wrap(super(__PropertiesUtil, self).getCharsetProperty(name))

    @overload
    def getBooleanProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Boolean':
        """public java.lang.Boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Boolean>)"""
        return 'Boolean'.__wrap(super(__PropertiesUtil, self).getBooleanProperty(prefixes, key, supplier))

    @overload
    def getDurationProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Duration':
        """public java.time.Duration org.apache.logging.log4j.util.PropertiesUtil.getDurationProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.time.Duration>)"""
        return 'Duration'.__wrap(super(__PropertiesUtil, self).getDurationProperty(prefixes, key, supplier))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isOsWindows(self) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.isOsWindows()"""
        return bool.__wrap(super(PropertiesUtil, self).isOsWindows())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def partitionOnCommonPrefixes(properties: 'Properties', includeBaseKey: bool) -> 'Map':
        """public static java.util.Map<java.lang.String, java.util.Properties> org.apache.logging.log4j.util.PropertiesUtil.partitionOnCommonPrefixes(java.util.Properties,boolean)"""
        return Map.__wrap(__PropertiesUtil.partitionOnCommonPrefixes(properties, __boolean.valueOf(includeBaseKey)))

    @overload
    def reload(self):
        """public void org.apache.logging.log4j.util.PropertiesUtil.reload()"""
        super(PropertiesUtil, self).reload()

    @overload
    def getCharsetProperty(self, name: str, defaultValue: 'Charset') -> 'Charset':
        """public java.nio.charset.Charset org.apache.logging.log4j.util.PropertiesUtil.getCharsetProperty(java.lang.String,java.nio.charset.Charset)"""
        return 'Charset'.__wrap(super(__PropertiesUtil, self).getCharsetProperty(name, defaultValue))

    @staticmethod
    @overload
    def getProperties() -> 'PropertiesUtil':
        """public static org.apache.logging.log4j.util.PropertiesUtil org.apache.logging.log4j.util.PropertiesUtil.getProperties()"""
        return PropertiesUtil.__wrap(__PropertiesUtil.getProperties())

    @staticmethod
    @overload
    def partitionOnCommonPrefixes(properties: 'Properties') -> 'Map':
        """public static java.util.Map<java.lang.String, java.util.Properties> org.apache.logging.log4j.util.PropertiesUtil.partitionOnCommonPrefixes(java.util.Properties)"""
        return Map.__wrap(__PropertiesUtil.partitionOnCommonPrefixes(properties))

    @staticmethod
    @overload
    def getSystemProperties() -> 'Properties':
        """public static java.util.Properties org.apache.logging.log4j.util.PropertiesUtil.getSystemProperties()"""
        return Properties.__wrap(__PropertiesUtil.getSystemProperties())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getIntegerProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Integer':
        """public java.lang.Integer org.apache.logging.log4j.util.PropertiesUtil.getIntegerProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Integer>)"""
        return __transform(super(__PropertiesUtil, self).getIntegerProperty(prefixes, key, supplier)).'Integer'Value()

    @overload
    def addPropertySource(self, propertySource: 'PropertySource'):
        """public void org.apache.logging.log4j.util.PropertiesUtil.addPropertySource(org.apache.logging.log4j.util.PropertySource)"""
        super(__PropertiesUtil, self).addPropertySource(propertySource) 
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource$Util
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.util.PropertySource as __PropertySource_Util
__Util = __PropertySource_Util.Util
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class Util():
    """org.apache.logging.log4j.util.PropertySource.Util"""
 
    @staticmethod
    def __wrap(java_value: __Util) -> 'Util':
        return Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Util):
        """
        Dynamic initializer for Util.
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

    @staticmethod
    @overload
    def tokenize(value: 'CharSequence') -> 'List':
        """public static java.util.List<java.lang.CharSequence> org.apache.logging.log4j.util.PropertySource$Util.tokenize(java.lang.CharSequence)"""
        return List.__wrap(__Util.tokenize(value))

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

    @staticmethod
    @overload
    def joinAsCamelCase(tokens: 'Iterable') -> 'CharSequence':
        """public static java.lang.CharSequence org.apache.logging.log4j.util.PropertySource$Util.joinAsCamelCase(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return CharSequence.__wrap(__Util.joinAsCamelCase(tokens))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.LoaderUtil
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.util.LoaderUtil as __LoaderUtil
__LoaderUtil = __LoaderUtil
import java.lang.ClassLoader as __ClassLoader
__ClassLoader = __ClassLoader
import java.util.Collection as Collection
from builtins import object
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoaderUtil():
    """org.apache.logging.log4j.util.LoaderUtil"""
 
    @staticmethod
    def __wrap(java_value: __LoaderUtil) -> 'LoaderUtil':
        return LoaderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoaderUtil):
        """
        Dynamic initializer for LoaderUtil.
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
 
    @staticmethod
    @overload
    def newCheckedInstanceOfProperty(propertyName: str, clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOfProperty(java.lang.String,java.lang.Class<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object.__wrap(__LoaderUtil.newCheckedInstanceOfProperty(propertyName, clazz))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def newInstanceOf(clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOf(java.lang.Class<T>) throws java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.NoSuchMethodException"""
        return object.__wrap(__LoaderUtil.newInstanceOf(clazz))

    @staticmethod
    @overload
    def newInstanceOfUnchecked(className: str, supertype: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.String,java.lang.Class<T>)"""
        return object.__wrap(__LoaderUtil.newInstanceOfUnchecked(className, supertype))

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

    @staticmethod
    @overload
    def newCheckedInstanceOf(className: str, clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOf(java.lang.String,java.lang.Class<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object.__wrap(__LoaderUtil.newCheckedInstanceOf(className, clazz))

    @staticmethod
    @overload
    def newInstanceOfUnchecked(className: str) -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.String)"""
        return object.__wrap(__LoaderUtil.newInstanceOfUnchecked(className))

    @staticmethod
    @overload
    def newInstanceOf(className: str) -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOf(java.lang.String) throws java.lang.ClassNotFoundException,java.lang.IllegalAccessException,java.lang.InstantiationException,java.lang.reflect.InvocationTargetException,java.lang.NoSuchMethodException"""
        return object.__wrap(__LoaderUtil.newInstanceOf(className))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getClassLoader()"""
        return ClassLoader.__wrap(__LoaderUtil.getClassLoader())

    @staticmethod
    @overload
    def findResources(resource: str) -> 'Collection':
        """public static java.util.Collection<java.net.URL> org.apache.logging.log4j.util.LoaderUtil.findResources(java.lang.String)"""
        return Collection.__wrap(__LoaderUtil.findResources(resource))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def newCheckedInstanceOfProperty(propertyName: str, clazz: 'Class', defaultSupplier: 'Supplier') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOfProperty(java.lang.String,java.lang.Class<T>,java.util.function.Supplier<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object.__wrap(__LoaderUtil.newCheckedInstanceOfProperty(propertyName, clazz, defaultSupplier))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isClassAvailable(className: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.LoaderUtil.isClassAvailable(java.lang.String)"""
        return bool.__wrap(__LoaderUtil.isClassAvailable(className))

    @staticmethod
    @overload
    def newInstanceOfUnchecked(clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.Class<T>)"""
        return object.__wrap(__LoaderUtil.newInstanceOfUnchecked(clazz))

    @staticmethod
    @overload
    def getClassLoader(class1: 'Class', class2: 'Class') -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getClassLoader(java.lang.Class<?>,java.lang.Class<?>)"""
        return ClassLoader.__wrap(__LoaderUtil.getClassLoader(class1, class2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getThreadContextClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getThreadContextClassLoader()"""
        return ClassLoader.__wrap(__LoaderUtil.getThreadContextClassLoader())

    @staticmethod
    @overload
    def loadClassUnchecked(className: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.LoaderUtil.loadClassUnchecked(java.lang.String)"""
        return type.Class.__wrap(__LoaderUtil.loadClassUnchecked(className))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def loadClass(className: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.LoaderUtil.loadClass(java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class.__wrap(__LoaderUtil.loadClass(className))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.TriConsumer
import org.apache.logging.log4j.util.TriConsumer as __TriConsumer
__TriConsumer = __TriConsumer
from abc import abstractmethod, ABC
 
class TriConsumer(ABC):
    """org.apache.logging.log4j.util.TriConsumer"""
 
    @staticmethod
    def __wrap(java_value: __TriConsumer) -> 'TriConsumer':
        return TriConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TriConsumer):
        """
        Dynamic initializer for TriConsumer.
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
    def accept(self, k: object, v: object, s: object):
        """public abstract void org.apache.logging.log4j.util.TriConsumer.accept(K,V,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.FilteredObjectInputStream
import org.apache.logging.log4j.util.FilteredObjectInputStream as __FilteredObjectInputStream
__FilteredObjectInputStream = __FilteredObjectInputStream
from builtins import type
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.io.ObjectInputValidation as ObjectInputValidation
import java.io.ObjectInputStream.GetField as GetField
import java.io.ObjectInputFilter as ObjectInputFilter
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.io.ObjectInputStream as __ObjectInputStream_GetField
__GetField = __ObjectInputStream_GetField.GetField
import java.lang.Object as __object
from builtins import float
import java.io.ObjectInputStream as __ObjectInputStream
__ObjectInputStream = __ObjectInputStream
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import java.io.ObjectInputFilter as __ObjectInputFilter
__ObjectInputFilter = __ObjectInputFilter
import java.lang.Integer as __int
from builtins import int
 
class FilteredObjectInputStream():
    """org.apache.logging.log4j.util.FilteredObjectInputStream"""
 
    @staticmethod
    def __wrap(java_value: __FilteredObjectInputStream) -> 'FilteredObjectInputStream':
        return FilteredObjectInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FilteredObjectInputStream):
        """
        Dynamic initializer for FilteredObjectInputStream.
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
    def skip(self, arg0: int) -> int:
        """public long java.io.InputStream.skip(long) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).skip(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream.__wrap(__InputStream.nullInputStream())

    @overload
    def __init__(self, allowedExtraClasses: 'Collection'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.util.Collection<java.lang.String>) throws java.io.IOException,java.lang.SecurityException"""
        val = __FilteredObjectInputStream(allowedExtraClasses)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def readLong(self) -> int:
        """public long java.io.ObjectInputStream.readLong() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readLong())

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.InputStream.markSupported()"""
        return bool.__wrap(super(InputStream, self).markSupported())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream() throws java.io.IOException,java.lang.SecurityException"""
        val = __FilteredObjectInputStream()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def readShort(self) -> int:
        """public short java.io.ObjectInputStream.readShort() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readShort())

    @override
    @overload
    def reset(self):
        """public void java.io.InputStream.reset() throws java.io.IOException"""
        super(InputStream, self).reset()

    @overload
    def skipBytes(self, arg0: int) -> int:
        """public int java.io.ObjectInputStream.skipBytes(int) throws java.io.IOException"""
        return int.__wrap(super(__ObjectInputStream, self).skipBytes(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, inputStream: 'InputStream', allowedExtraClasses: 'Collection'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.io.InputStream,java.util.Collection<java.lang.String>) throws java.io.IOException"""
        val = __FilteredObjectInputStream(inputStream, allowedExtraClasses)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, inputStream: 'InputStream'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.io.InputStream) throws java.io.IOException"""
        val = __FilteredObjectInputStream(inputStream)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def readBoolean(self) -> bool:
        """public boolean java.io.ObjectInputStream.readBoolean() throws java.io.IOException"""
        return bool.__wrap(super(ObjectInputStream, self).readBoolean())

    @override
    @overload
    def setObjectInputFilter(self, arg0: 'ObjectInputFilter'):
        """public final void java.io.ObjectInputStream.setObjectInputFilter(java.io.ObjectInputFilter)"""
        super(__ObjectInputStream, self).setObjectInputFilter(arg0)

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).transferTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def readDouble(self) -> float:
        """public double java.io.ObjectInputStream.readDouble() throws java.io.IOException"""
        return float.__wrap(super(ObjectInputStream, self).readDouble())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int].__wrap(super(__InputStream, self).readNBytes(__int.valueOf(arg0)))

    @override
    @overload
    def readObject(self) -> object:
        """public final java.lang.Object java.io.ObjectInputStream.readObject() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object.__wrap(super(ObjectInputStream, self).readObject())

    @override
    @overload
    def readFloat(self) -> float:
        """public float java.io.ObjectInputStream.readFloat() throws java.io.IOException"""
        return float.__wrap(super(ObjectInputStream, self).readFloat())

    @override
    @overload
    def defaultReadObject(self):
        """public void java.io.ObjectInputStream.defaultReadObject() throws java.io.IOException,java.lang.ClassNotFoundException"""
        super(ObjectInputStream, self).defaultReadObject()

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.InputStream.read(byte[]) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).read(bytes))

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(__InputStream, self).skipNBytes(__long.valueOf(arg0))

    @override
    @overload
    def readUTF(self) -> str:
        """public java.lang.String java.io.ObjectInputStream.readUTF() throws java.io.IOException"""
        return str.__wrap(super(ObjectInputStream, self).readUTF())

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.InputStream.mark(int)"""
        super(__InputStream, self).mark(__int.valueOf(arg0))

    @override
    @overload
    def registerValidation(self, arg0: 'ObjectInputValidation', arg1: int):
        """public void java.io.ObjectInputStream.registerValidation(java.io.ObjectInputValidation,int) throws java.io.NotActiveException,java.io.InvalidObjectException"""
        super(__ObjectInputStream, self).registerValidation(arg0, __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def readUnshared(self) -> object:
        """public java.lang.Object java.io.ObjectInputStream.readUnshared() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object.__wrap(super(ObjectInputStream, self).readUnshared())

    @override
    @overload
    def readByte(self) -> int:
        """public byte java.io.ObjectInputStream.readByte() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readByte())

    @override
    @overload
    def readUnsignedByte(self) -> int:
        """public int java.io.ObjectInputStream.readUnsignedByte() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readUnsignedByte())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.ObjectInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__ObjectInputStream, self).read(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getAllowedClasses(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.FilteredObjectInputStream.getAllowedClasses()"""
        return 'Collection'.__wrap(super(FilteredObjectInputStream, self).getAllowedClasses())

    @override
    @overload
    def readFully(self, arg0: bytes):
        """public void java.io.ObjectInputStream.readFully(byte[]) throws java.io.IOException"""
        super(__ObjectInputStream, self).readFully(bytes)

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int].__wrap(super(InputStream, self).readAllBytes())

    @override
    @overload
    def readChar(self) -> str:
        """public char java.io.ObjectInputStream.readChar() throws java.io.IOException"""
        return str.__wrap(super(ObjectInputStream, self).readChar())

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public int java.io.ObjectInputStream.readUnsignedShort() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readUnsignedShort())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def available(self) -> int:
        """public int java.io.ObjectInputStream.available() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).available())

    @override
    @overload
    def getObjectInputFilter(self) -> 'ObjectInputFilter':
        """public final java.io.ObjectInputFilter java.io.ObjectInputStream.getObjectInputFilter()"""
        return 'ObjectInputFilter'.__wrap(super(ObjectInputStream, self).getObjectInputFilter())

    @override
    @overload
    def close(self):
        """public void java.io.ObjectInputStream.close() throws java.io.IOException"""
        super(ObjectInputStream, self).close()

    @override
    @overload
    def readFields(self) -> 'GetField.ObjectInputStream$GetField':
        """public java.io.ObjectInputStream$GetField java.io.ObjectInputStream.readFields() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return 'GetField.ObjectInputStream$GetField'.__wrap(super(ObjectInputStream, self).readFields())

    @override
    @overload
    def read(self) -> int:
        """public int java.io.ObjectInputStream.read() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).read())

    @override
    @overload
    def readInt(self) -> int:
        """public int java.io.ObjectInputStream.readInt() throws java.io.IOException"""
        return int.__wrap(super(ObjectInputStream, self).readInt())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream() throws java.io.IOException,java.lang.SecurityException"""
        val = __FilteredObjectInputStream()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int.__wrap(super(__InputStream, self).readNBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

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
    def readLine(self) -> str:
        """public java.lang.String java.io.ObjectInputStream.readLine() throws java.io.IOException"""
        return str.__wrap(super(ObjectInputStream, self).readLine())

    @override
    @overload
    def readFully(self, arg0: bytes, arg1: int, arg2: int):
        """public void java.io.ObjectInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(__ObjectInputStream, self).readFully(bytes, __int.valueOf(arg1), __int.valueOf(arg2)) 
 
 
# CLASS: org.apache.logging.log4j.util.StackLocatorUtil
import java.util.function.Predicate as Predicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
import java.lang.ClassLoader as __ClassLoader
__ClassLoader = __ClassLoader
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import org.apache.logging.log4j.util.StackLocatorUtil as __StackLocatorUtil
__StackLocatorUtil = __StackLocatorUtil
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StackLocatorUtil():
    """org.apache.logging.log4j.util.StackLocatorUtil"""
 
    @staticmethod
    def __wrap(java_value: __StackLocatorUtil) -> 'StackLocatorUtil':
        return StackLocatorUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StackLocatorUtil):
        """
        Dynamic initializer for StackLocatorUtil.
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
 
    @staticmethod
    @overload
    def getCallerClass(fqcn: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.String)"""
        return type.Class.__wrap(__StackLocatorUtil.getCallerClass(fqcn))

    @staticmethod
    @overload
    def getStackTraceElement(depth: int) -> 'StackTraceElement':
        """public static java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocatorUtil.getStackTraceElement(int)"""
        return StackTraceElement.__wrap(__StackLocatorUtil.getStackTraceElement(__int.valueOf(depth)))

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

    @staticmethod
    @overload
    def calcLocation(fqcnOfLogger: str) -> 'StackTraceElement':
        """public static java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocatorUtil.calcLocation(java.lang.String)"""
        return StackTraceElement.__wrap(__StackLocatorUtil.calcLocation(fqcnOfLogger))

    @staticmethod
    @overload
    def getCallerClassLoader(depth: int) -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.StackLocatorUtil.getCallerClassLoader(int)"""
        return ClassLoader.__wrap(__StackLocatorUtil.getCallerClassLoader(__int.valueOf(depth)))

    @staticmethod
    @overload
    def getCallerClass(depth: int) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(int)"""
        return type.Class.__wrap(__StackLocatorUtil.getCallerClass(__int.valueOf(depth)))

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

    @staticmethod
    @overload
    def getCallerClass(anchor: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.Class<?>)"""
        return type.Class.__wrap(__StackLocatorUtil.getCallerClass(anchor))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getCallerClass(fqcn: str, pkg: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.String,java.lang.String)"""
        return type.Class.__wrap(__StackLocatorUtil.getCallerClass(fqcn, pkg))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getCallerClass(sentinelClass: 'Class', callerPredicate: 'Predicate') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.Class<?>,java.util.function.Predicate<java.lang.Class<?>>)"""
        return type.Class.__wrap(__StackLocatorUtil.getCallerClass(sentinelClass, callerPredicate))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getCurrentStackTrace() -> 'Deque':
        """public static java.util.Deque<java.lang.Class<?>> org.apache.logging.log4j.util.StackLocatorUtil.getCurrentStackTrace()"""
        return Deque.__wrap(__StackLocatorUtil.getCurrentStackTrace())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.IndexedReadOnlyStringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as __ReadOnlyStringMap
__ReadOnlyStringMap = __ReadOnlyStringMap
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as __IndexedReadOnlyStringMap
__IndexedReadOnlyStringMap = __IndexedReadOnlyStringMap
 
class IndexedReadOnlyStringMap(ABC):
    """org.apache.logging.log4j.util.IndexedReadOnlyStringMap"""
 
    @staticmethod
    def __wrap(java_value: __IndexedReadOnlyStringMap) -> 'IndexedReadOnlyStringMap':
        return IndexedReadOnlyStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedReadOnlyStringMap):
        """
        Dynamic initializer for IndexedReadOnlyStringMap.
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
    def indexOfKey(self, key: str):
        """public abstract int org.apache.logging.log4j.util.IndexedReadOnlyStringMap.indexOfKey(java.lang.String)"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def getKeyAt(self, index: int):
        """public abstract java.lang.String org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getKeyAt(int)"""
        pass

    @abstractmethod
    def getValueAt(self, index: int):
        """public abstract <V> V org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getValueAt(int)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.Supplier
import org.apache.logging.log4j.util.Supplier as __Supplier
__Supplier = __Supplier
from abc import abstractmethod, ABC
 
class Supplier(ABC):
    """org.apache.logging.log4j.util.Supplier"""
 
    @staticmethod
    def __wrap(java_value: __Supplier) -> 'Supplier':
        return Supplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Supplier):
        """
        Dynamic initializer for Supplier.
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
    def get(self, ):
        """public abstract T org.apache.logging.log4j.util.Supplier.get()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.Strings
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Iterator as Iterator
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.logging.log4j.util.Strings as __Strings
__Strings = __Strings
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Strings():
    """org.apache.logging.log4j.util.Strings"""
 
    @staticmethod
    def __wrap(java_value: __Strings) -> 'Strings':
        return Strings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Strings):
        """
        Dynamic initializer for Strings.
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

    @staticmethod
    @overload
    def splitList(string: str) -> List[str]:
        """public static java.lang.String[] org.apache.logging.log4j.util.Strings.splitList(java.lang.String)"""
        return List[str].__wrap(__Strings.splitList(string))

    @staticmethod
    @overload
    def toRootUpperCase(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.toRootUpperCase(java.lang.String)"""
        return str.__wrap(__Strings.toRootUpperCase(str))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isNotBlank(s: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isNotBlank(java.lang.String)"""
        return bool.__wrap(__Strings.isNotBlank(s))

    @staticmethod
    @overload
    def left(str: str, len: int) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.left(java.lang.String,int)"""
        return str.__wrap(__Strings.left(str, __int.valueOf(len)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def quote(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.quote(java.lang.String)"""
        return str.__wrap(__Strings.quote(str))

    @staticmethod
    @overload
    def join(iterator: 'Iterator', separator: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.join(java.util.Iterator<?>,char)"""
        return str.__wrap(__Strings.join(iterator, __char.valueOf(separator)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def repeat(str: str, count: int) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.repeat(java.lang.String,int)"""
        return str.__wrap(__Strings.repeat(str, __int.valueOf(count)))

    @staticmethod
    @overload
    def isBlank(s: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isBlank(java.lang.String)"""
        return bool.__wrap(__Strings.isBlank(s))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def isNotEmpty(cs: 'CharSequence') -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isNotEmpty(java.lang.CharSequence)"""
        return bool.__wrap(__Strings.isNotEmpty(cs))

    @staticmethod
    @overload
    def trimToNull(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.trimToNull(java.lang.String)"""
        return str.__wrap(__Strings.trimToNull(str))

    @staticmethod
    @overload
    def concat(str1: str, str2: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.concat(java.lang.String,java.lang.String)"""
        return str.__wrap(__Strings.concat(str1, str2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def join(iterable: 'Iterable', separator: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.join(java.lang.Iterable<?>,char)"""
        return str.__wrap(__Strings.join(iterable, __char.valueOf(separator)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def toRootLowerCase(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.toRootLowerCase(java.lang.String)"""
        return str.__wrap(__Strings.toRootLowerCase(str))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isEmpty(cs: 'CharSequence') -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isEmpty(java.lang.CharSequence)"""
        return bool.__wrap(__Strings.isEmpty(cs))

    @staticmethod
    @overload
    def dquote(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.dquote(java.lang.String)"""
        return str.__wrap(__Strings.dquote(str))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.Timer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import org.apache.logging.log4j.util.Timer as __Timer
__Timer = __Timer
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import org.apache.logging.log4j.util.Timer as __Timer_Status
__Status = __Timer_Status.Status
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Timer():
    """org.apache.logging.log4j.util.Timer"""
 
    @staticmethod
    def __wrap(java_value: __Timer) -> 'Timer':
        return Timer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Timer):
        """
        Dynamic initializer for Timer.
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
    def __init__(self, name: str, iterations: int):
        """public org.apache.logging.log4j.util.Timer(java.lang.String,int)"""
        val = __Timer(name, __int.valueOf(iterations))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getStatus(self) -> 'Status':
        """public org.apache.logging.log4j.util.Timer$Status org.apache.logging.log4j.util.Timer.getStatus()"""
        return 'Status'.__wrap(super(Timer, self).getStatus())

    @overload
    def stop(self) -> str:
        """public synchronized java.lang.String org.apache.logging.log4j.util.Timer.stop()"""
        return str.__wrap(super(Timer, self).stop())

    @overload
    def start(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.start()"""
        super(Timer, self).start()

    @overload
    def getElapsedNanoTime(self) -> int:
        """public long org.apache.logging.log4j.util.Timer.getElapsedNanoTime()"""
        return int.__wrap(super(Timer, self).getElapsedNanoTime())

    @overload
    def startOrResume(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.startOrResume()"""
        super(Timer, self).startOrResume()

    @overload
    def getElapsedTime(self) -> int:
        """public long org.apache.logging.log4j.util.Timer.getElapsedTime()"""
        return int.__wrap(super(Timer, self).getElapsedTime())

    @overload
    def pause(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.pause()"""
        super(Timer, self).pause()

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
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.Timer.toString()"""
        return str.__wrap(super(Timer, self).toString())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.util.Timer.equals(java.lang.Object)"""
        return bool.__wrap(super(__Timer, self).equals(o))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.util.Timer.formatTo(java.lang.StringBuilder)"""
        super(__Timer, self).formatTo(buffer)

    @overload
    def resume(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.resume()"""
        super(Timer, self).resume()

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.util.Timer(java.lang.String)"""
        val = __Timer(name)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.Timer.getName()"""
        return str.__wrap(super(Timer, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.util.Timer.hashCode()"""
        return int.__wrap(super(Timer, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.StackLocator
import java.util.function.Predicate as Predicate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Deque as Deque
import java.util.Deque as __Deque
__Deque = __Deque
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import java.lang.Long as __long
import org.apache.logging.log4j.util.StackLocator as __StackLocator
__StackLocator = __StackLocator
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
 
class StackLocator():
    """org.apache.logging.log4j.util.StackLocator"""
 
    @staticmethod
    def __wrap(java_value: __StackLocator) -> 'StackLocator':
        return StackLocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StackLocator):
        """
        Dynamic initializer for StackLocator.
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
    def getCallerClass(self, fqcn: str) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.String)"""
        return 'type.Class'.__wrap(super(__StackLocator, self).getCallerClass(fqcn))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCallerClass(self, depth: int) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(int)"""
        return 'type.Class'.__wrap(super(__StackLocator, self).getCallerClass(__int.valueOf(depth)))

    @overload
    def getStackTraceElement(self, depth: int) -> 'StackTraceElement':
        """public java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocator.getStackTraceElement(int)"""
        return 'StackTraceElement'.__wrap(super(__StackLocator, self).getStackTraceElement(__int.valueOf(depth)))

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
    def getCallerClass(self, fqcn: str, pkg: str) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.String,java.lang.String)"""
        return 'type.Class'.__wrap(super(__StackLocator, self).getCallerClass(fqcn, pkg))

    @overload
    def getCallerClass(self, anchor: 'Class') -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.Class<?>)"""
        return 'type.Class'.__wrap(super(__StackLocator, self).getCallerClass(anchor))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getInstance() -> 'StackLocator':
        """public static org.apache.logging.log4j.util.StackLocator org.apache.logging.log4j.util.StackLocator.getInstance()"""
        return StackLocator.__wrap(__StackLocator.getInstance())

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
    def getCurrentStackTrace(self) -> 'Deque':
        """public java.util.Deque<java.lang.Class<?>> org.apache.logging.log4j.util.StackLocator.getCurrentStackTrace()"""
        return 'Deque'.__wrap(super(StackLocator, self).getCurrentStackTrace())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def calcLocation(self, fqcnOfLogger: str) -> 'StackTraceElement':
        """public java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocator.calcLocation(java.lang.String)"""
        return 'StackTraceElement'.__wrap(super(__StackLocator, self).calcLocation(fqcnOfLogger))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getCallerClass(self, sentinelClass: 'Class', callerPredicate: 'Predicate') -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.Class<?>,java.util.function.Predicate<java.lang.Class<?>>)"""
        return 'type.Class'.__wrap(super(__StackLocator, self).getCallerClass(sentinelClass, callerPredicate)) 
 
 
# CLASS: org.apache.logging.log4j.util.ReadOnlyStringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as __ReadOnlyStringMap
__ReadOnlyStringMap = __ReadOnlyStringMap
 
class ReadOnlyStringMap(ABC):
    """org.apache.logging.log4j.util.ReadOnlyStringMap"""
 
    @staticmethod
    def __wrap(java_value: __ReadOnlyStringMap) -> 'ReadOnlyStringMap':
        return ReadOnlyStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReadOnlyStringMap):
        """
        Dynamic initializer for ReadOnlyStringMap.
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
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.ProviderUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.util.ProviderUtil as __ProviderUtil
__ProviderUtil = __ProviderUtil
import java.lang.Iterable as Iterable
import java.lang.ClassLoader as __ClassLoader
__ClassLoader = __ClassLoader
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class ProviderUtil():
    """org.apache.logging.log4j.util.ProviderUtil"""
 
    @staticmethod
    def __wrap(java_value: __ProviderUtil) -> 'ProviderUtil':
        return ProviderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProviderUtil):
        """
        Dynamic initializer for ProviderUtil.
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
    def getProviders() -> 'Iterable':
        """public static java.lang.Iterable<org.apache.logging.log4j.spi.Provider> org.apache.logging.log4j.util.ProviderUtil.getProviders()"""
        return Iterable.__wrap(__ProviderUtil.getProviders())

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

    @staticmethod
    @overload
    def hasProviders() -> bool:
        """public static boolean org.apache.logging.log4j.util.ProviderUtil.hasProviders()"""
        return bool.__wrap(__ProviderUtil.hasProviders())

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

    @staticmethod
    @overload
    def findClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.ProviderUtil.findClassLoader()"""
        return ClassLoader.__wrap(__ProviderUtil.findClassLoader())

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
 
 
# CLASS: org.apache.logging.log4j.util.PerformanceSensitive
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.PerformanceSensitive as __PerformanceSensitive
__PerformanceSensitive = __PerformanceSensitive
 
class PerformanceSensitive(ABC):
    """org.apache.logging.log4j.util.PerformanceSensitive"""
 
    @staticmethod
    def __wrap(java_value: __PerformanceSensitive) -> 'PerformanceSensitive':
        return PerformanceSensitive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerformanceSensitive):
        """
        Dynamic initializer for PerformanceSensitive.
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
    def value(self, ):
        """public abstract java.lang.String[] org.apache.logging.log4j.util.PerformanceSensitive.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource$Comparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.util.PropertySource as __PropertySource_Comparator
__Comparator = __PropertySource_Comparator.Comparator
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.function.ToIntFunction as ToIntFunction
import java.lang.Object as __Object
__Object = __Object
import java.util.function.ToLongFunction as ToLongFunction
import java.lang.Integer as __int
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
from builtins import int
 
class Comparator():
    """org.apache.logging.log4j.util.PropertySource.Comparator"""
 
    @staticmethod
    def __wrap(java_value: __Comparator) -> 'Comparator':
        return Comparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Comparator):
        """
        Dynamic initializer for Comparator.
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
    def compare(self, o1: 'PropertySource', o2: 'PropertySource') -> int:
        """public int org.apache.logging.log4j.util.PropertySource$Comparator.compare(org.apache.logging.log4j.util.PropertySource,org.apache.logging.log4j.util.PropertySource)"""
        return int.__wrap(super(__Comparator, self).compare(o1, o2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.PropertySource$Comparator()"""
        val = __Comparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.PropertySource$Comparator()"""
        val = __Comparator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'.__wrap(super(Comparator, self).reversed())

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
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingInt(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingLong(arg0))

    @overload
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparing(arg0, arg1))

    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'.__wrap(super(__Comparator, self).thenComparingDouble(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource
from builtins import str
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.CharSequence as CharSequence
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Iterable as Iterable
import org.apache.logging.log4j.util.PropertySource as __PropertySource
__PropertySource = __PropertySource
import java.util.Collection as Collection
from abc import abstractmethod, ABC
from builtins import bool
 
class PropertySource(ABC):
    """org.apache.logging.log4j.util.PropertySource"""
 
    @staticmethod
    def __wrap(java_value: __PropertySource) -> 'PropertySource':
        return PropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertySource):
        """
        Dynamic initializer for PropertySource.
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
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public default java.lang.CharSequence org.apache.logging.log4j.util.PropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__PropertySource, self).getNormalForm(tokens))

    @overload
    def forEach(self, action: 'BiConsumer'):
        """public default void org.apache.logging.log4j.util.PropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__PropertySource, self).forEach(action)

    @overload
    def getProperty(self, key: str) -> str:
        """public default java.lang.String org.apache.logging.log4j.util.PropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__PropertySource, self).getProperty(key))

    @abstractmethod
    def getPriority(self, ):
        """public abstract int org.apache.logging.log4j.util.PropertySource.getPriority()"""
        pass

    @overload
    def containsProperty(self, key: str) -> bool:
        """public default boolean org.apache.logging.log4j.util.PropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__PropertySource, self).containsProperty(key))

    @overload
    def getPropertyNames(self) -> 'Collection':
        """public default java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(PropertySource, self).getPropertyNames()) 
 
 
# CLASS: org.apache.logging.log4j.util.ServiceLoaderUtil
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.apache.logging.log4j.util.ServiceLoaderUtil as __ServiceLoaderUtil
__ServiceLoaderUtil = __ServiceLoaderUtil
import java.lang.Integer as __int
from builtins import bool
import java.lang.invoke.MethodHandles.Lookup as Lookup
from builtins import int
 
class ServiceLoaderUtil():
    """org.apache.logging.log4j.util.ServiceLoaderUtil"""
 
    @staticmethod
    def __wrap(java_value: __ServiceLoaderUtil) -> 'ServiceLoaderUtil':
        return ServiceLoaderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServiceLoaderUtil):
        """
        Dynamic initializer for ServiceLoaderUtil.
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
 
    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup', useTccl: bool) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.ServiceLoaderUtil.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup,boolean)"""
        return Stream.__wrap(__ServiceLoaderUtil.loadServices(serviceType, lookup, __boolean.valueOf(useTccl)))

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

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup') -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.ServiceLoaderUtil.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup)"""
        return Stream.__wrap(__ServiceLoaderUtil.loadServices(serviceType, lookup))

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
 
 
# CLASS: org.apache.logging.log4j.util.BiConsumer
import org.apache.logging.log4j.util.BiConsumer as __BiConsumer
__BiConsumer = __BiConsumer
from abc import abstractmethod, ABC
 
class BiConsumer(ABC):
    """org.apache.logging.log4j.util.BiConsumer"""
 
    @staticmethod
    def __wrap(java_value: __BiConsumer) -> 'BiConsumer':
        return BiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BiConsumer):
        """
        Dynamic initializer for BiConsumer.
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
    def accept(self, k: object, v: object):
        """public abstract void org.apache.logging.log4j.util.BiConsumer.accept(K,V)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.EnglishEnums
import org.apache.logging.log4j.util.EnglishEnums as __EnglishEnums
__EnglishEnums = __EnglishEnums
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class EnglishEnums():
    """org.apache.logging.log4j.util.EnglishEnums"""
 
    @staticmethod
    def __wrap(java_value: __EnglishEnums) -> 'EnglishEnums':
        return EnglishEnums(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnglishEnums):
        """
        Dynamic initializer for EnglishEnums.
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

    @staticmethod
    @overload
    def valueOf(enumType: 'Class', name: str, defaultValue: 'Enum') -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T org.apache.logging.log4j.util.EnglishEnums.valueOf(java.lang.Class<T>,java.lang.String,T)"""
        return Enum.__wrap(__EnglishEnums.valueOf(enumType, name, defaultValue))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def valueOf(enumType: 'Class', name: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T org.apache.logging.log4j.util.EnglishEnums.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__EnglishEnums.valueOf(enumType, name))

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
 
 
# CLASS: org.apache.logging.log4j.util.Base64Util
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.util.Base64Util as __Base64Util
__Base64Util = __Base64Util
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Base64Util():
    """org.apache.logging.log4j.util.Base64Util"""
 
    @staticmethod
    def __wrap(java_value: __Base64Util) -> 'Base64Util':
        return Base64Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Base64Util):
        """
        Dynamic initializer for Base64Util.
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

    @staticmethod
    @overload
    def encode(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Base64Util.encode(java.lang.String)"""
        return str.__wrap(__Base64Util.encode(str))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.EnvironmentPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.util.EnvironmentPropertySource as __EnvironmentPropertySource
__EnvironmentPropertySource = __EnvironmentPropertySource
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EnvironmentPropertySource():
    """org.apache.logging.log4j.util.EnvironmentPropertySource"""
 
    @staticmethod
    def __wrap(java_value: __EnvironmentPropertySource) -> 'EnvironmentPropertySource':
        return EnvironmentPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnvironmentPropertySource):
        """
        Dynamic initializer for EnvironmentPropertySource.
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
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.EnvironmentPropertySource.containsProperty(java.lang.String)"""
        return bool.__wrap(super(__EnvironmentPropertySource, self).containsProperty(key))

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.EnvironmentPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(__EnvironmentPropertySource, self).forEach(action)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.EnvironmentPropertySource.getPriority()"""
        return int.__wrap(super(EnvironmentPropertySource, self).getPriority())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.EnvironmentPropertySource()"""
        val = __EnvironmentPropertySource()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.EnvironmentPropertySource()"""
        val = __EnvironmentPropertySource()
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
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.EnvironmentPropertySource.getPropertyNames()"""
        return 'Collection'.__wrap(super(EnvironmentPropertySource, self).getPropertyNames())

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
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.EnvironmentPropertySource.getProperty(java.lang.String)"""
        return str.__wrap(super(__EnvironmentPropertySource, self).getProperty(key))

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.EnvironmentPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'.__wrap(super(__EnvironmentPropertySource, self).getNormalForm(tokens))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.Cast
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.util.Cast as __Cast
__Cast = __Cast
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Cast():
    """org.apache.logging.log4j.util.Cast"""
 
    @staticmethod
    def __wrap(java_value: __Cast) -> 'Cast':
        return Cast(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cast):
        """
        Dynamic initializer for Cast.
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

    @staticmethod
    @overload
    def cast(o: object) -> object:
        """public static <T> T org.apache.logging.log4j.util.Cast.cast(java.lang.Object)"""
        return object.__wrap(__Cast.cast(o))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.IndexedStringMap
import org.apache.logging.log4j.util.StringMap as __StringMap
__StringMap = __StringMap
import org.apache.logging.log4j.util.IndexedStringMap as __IndexedStringMap
__IndexedStringMap = __IndexedStringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as __ReadOnlyStringMap
__ReadOnlyStringMap = __ReadOnlyStringMap
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as __IndexedReadOnlyStringMap
__IndexedReadOnlyStringMap = __IndexedReadOnlyStringMap
 
class IndexedStringMap(ABC):
    """org.apache.logging.log4j.util.IndexedStringMap"""
 
    @staticmethod
    def __wrap(java_value: __IndexedStringMap) -> 'IndexedStringMap':
        return IndexedStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedStringMap):
        """
        Dynamic initializer for IndexedStringMap.
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
    def hashCode(self, ):
        """public abstract int org.apache.logging.log4j.util.StringMap.hashCode()"""
        pass

    @abstractmethod
    def freeze(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.freeze()"""
        pass

    @abstractmethod
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public abstract void org.apache.logging.log4j.util.StringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.clear()"""
        pass

    @abstractmethod
    def indexOfKey(self, key: str):
        """public abstract int org.apache.logging.log4j.util.IndexedReadOnlyStringMap.indexOfKey(java.lang.String)"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def getKeyAt(self, index: int):
        """public abstract java.lang.String org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getKeyAt(int)"""
        pass

    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract void org.apache.logging.log4j.util.StringMap.putValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def getValueAt(self, index: int):
        """public abstract <V> V org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getValueAt(int)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.util.StringMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass

    @abstractmethod
    def isFrozen(self, ):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.isFrozen()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.InternalException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.util.InternalException as __InternalException
__InternalException = __InternalException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InternalException():
    """org.apache.logging.log4j.util.InternalException"""
 
    @staticmethod
    def __wrap(java_value: __InternalException) -> 'InternalException':
        return InternalException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InternalException):
        """
        Dynamic initializer for InternalException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public org.apache.logging.log4j.util.InternalException(java.lang.String,java.lang.Throwable)"""
        val = __InternalException(message, cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, message: str):
        """public org.apache.logging.log4j.util.InternalException(java.lang.String)"""
        val = __InternalException(message)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, cause: 'Throwable'):
        """public org.apache.logging.log4j.util.InternalException(java.lang.Throwable)"""
        val = __InternalException(cause)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: org.apache.logging.log4j.util.Lazy
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.util.Lazy as __Lazy
__Lazy = __Lazy
from builtins import object
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Lazy(ABC):
    """org.apache.logging.log4j.util.Lazy"""
 
    @staticmethod
    def __wrap(java_value: __Lazy) -> 'Lazy':
        return Lazy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Lazy):
        """
        Dynamic initializer for Lazy.
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
    def map(self, function: 'Function') -> 'Lazy':
        """public default <R> org.apache.logging.log4j.util.Lazy<R> org.apache.logging.log4j.util.Lazy.map(java.util.function.Function<? super T, ? extends R>)"""
        return 'Lazy'.__wrap(super(__Lazy, self).map(function))

    @abstractmethod
    def set(self, newValue: object):
        """public abstract void org.apache.logging.log4j.util.Lazy.set(T)"""
        pass

    @abstractmethod
    def value(self, ):
        """public abstract T org.apache.logging.log4j.util.Lazy.value()"""
        pass

    @staticmethod
    @overload
    def value(value: object) -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.value(T)"""
        return Lazy.__wrap(__Lazy.value(value))

    @staticmethod
    @overload
    def lazy(supplier: 'Supplier') -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.lazy(java.util.function.Supplier<T>)"""
        return Lazy.__wrap(__Lazy.lazy(supplier))

    @abstractmethod
    def isInitialized(self, ):
        """public abstract boolean org.apache.logging.log4j.util.Lazy.isInitialized()"""
        pass

    @override
    @overload
    def get(self) -> object:
        """public default T org.apache.logging.log4j.util.Lazy.get()"""
        return object.__wrap(super(Lazy, self).get())

    @staticmethod
    @overload
    def pure(supplier: 'Supplier') -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.pure(java.util.function.Supplier<T>)"""
        return Lazy.__wrap(__Lazy.pure(supplier))

    @staticmethod
    @overload
    def weak(value: object) -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.weak(T)"""
        return Lazy.__wrap(__Lazy.weak(value)) 
 
 
# CLASS: org.apache.logging.log4j.util.Unbox
from builtins import str
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.lang.Double as __double
import org.apache.logging.log4j.util.Unbox as __Unbox
__Unbox = __Unbox
from builtins import bool
from builtins import int
 
class Unbox():
    """org.apache.logging.log4j.util.Unbox"""
 
    @staticmethod
    def __wrap(java_value: __Unbox) -> 'Unbox':
        return Unbox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Unbox):
        """
        Dynamic initializer for Unbox.
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

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(short)"""
        return StringBuilder.__wrap(__Unbox.box(__short.valueOf(value)))

    @staticmethod
    @overload
    def box(value: str) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(char)"""
        return StringBuilder.__wrap(__Unbox.box(__char.valueOf(value)))

    @staticmethod
    @overload
    def box(value: float) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(float)"""
        return StringBuilder.__wrap(__Unbox.box(__float.valueOf(value)))

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

    @staticmethod
    @overload
    def box(value: bool) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(boolean)"""
        return StringBuilder.__wrap(__Unbox.box(__boolean.valueOf(value)))

    @staticmethod
    @overload
    def box(value: float) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(double)"""
        return StringBuilder.__wrap(__Unbox.box(__double.valueOf(value)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(int)"""
        return StringBuilder.__wrap(__Unbox.box(__int.valueOf(value)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(long)"""
        return StringBuilder.__wrap(__Unbox.box(__long.valueOf(value)))

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(byte)"""
        return StringBuilder.__wrap(__Unbox.box(__byte.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.SortedArrayStringMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.logging.log4j.util.SortedArrayStringMap as __SortedArrayStringMap
__SortedArrayStringMap = __SortedArrayStringMap
from builtins import object
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
 
class SortedArrayStringMap():
    """org.apache.logging.log4j.util.SortedArrayStringMap"""
 
    @staticmethod
    def __wrap(java_value: __SortedArrayStringMap) -> 'SortedArrayStringMap':
        return SortedArrayStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedArrayStringMap):
        """
        Dynamic initializer for SortedArrayStringMap.
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
    def clear(self):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.clear()"""
        super(SortedArrayStringMap, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.SortedArrayStringMap.toMap()"""
        return 'Map'.__wrap(super(SortedArrayStringMap, self).toMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SortedArrayStringMap.toString()"""
        return str.__wrap(super(SortedArrayStringMap, self).toString())

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.size()"""
        return int.__wrap(super(SortedArrayStringMap, self).size())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.hashCode()"""
        return int.__wrap(super(SortedArrayStringMap, self).hashCode())

    @override
    @overload
    def isFrozen(self) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.isFrozen()"""
        return bool.__wrap(super(SortedArrayStringMap, self).isFrozen())

    @override
    @overload
    def putValue(self, key: str, value: object):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.putValue(java.lang.String,java.lang.Object)"""
        super(__SortedArrayStringMap, self).putValue(key, value)

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.equals(java.lang.Object)"""
        return bool.__wrap(super(__SortedArrayStringMap, self).equals(obj))

    @overload
    def getKeyAt(self, index: int) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SortedArrayStringMap.getKeyAt(int)"""
        return str.__wrap(super(__SortedArrayStringMap, self).getKeyAt(__int.valueOf(index)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        super(__SortedArrayStringMap, self).putAll(source)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.SortedArrayStringMap()"""
        val = __SortedArrayStringMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <V,T> void org.apache.logging.log4j.util.SortedArrayStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, T>,T)"""
        super(__SortedArrayStringMap, self).forEach(action, state)

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(java.util.Map<java.lang.String, ?>)"""
        val = __SortedArrayStringMap(map)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, other: 'ReadOnlyStringMap'):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        val = __SortedArrayStringMap(other)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.SortedArrayStringMap()"""
        val = __SortedArrayStringMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getValue(self, key: str) -> object:
        """public <V> V org.apache.logging.log4j.util.SortedArrayStringMap.getValue(java.lang.String)"""
        return object.__wrap(super(__SortedArrayStringMap, self).getValue(key))

    @overload
    def getValueAt(self, index: int) -> object:
        """public <V> V org.apache.logging.log4j.util.SortedArrayStringMap.getValueAt(int)"""
        return object.__wrap(super(__SortedArrayStringMap, self).getValueAt(__int.valueOf(index)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.containsKey(java.lang.String)"""
        return bool.__wrap(super(__SortedArrayStringMap, self).containsKey(key))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.remove(java.lang.String)"""
        super(__SortedArrayStringMap, self).remove(key)

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.isEmpty()"""
        return bool.__wrap(super(SortedArrayStringMap, self).isEmpty())

    @overload
    def indexOfKey(self, key: str) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.indexOfKey(java.lang.String)"""
        return int.__wrap(super(__SortedArrayStringMap, self).indexOfKey(key))

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(int)"""
        val = __SortedArrayStringMap(__int.valueOf(initialCapacity))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def freeze(self):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.freeze()"""
        super(SortedArrayStringMap, self).freeze()

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <V> void org.apache.logging.log4j.util.SortedArrayStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        super(__SortedArrayStringMap, self).forEach(action) 
 
 
# CLASS: org.apache.logging.log4j.util.Chars
from builtins import str
import java.lang.Long as __long
import org.apache.logging.log4j.util.Chars as __Chars
__Chars = __Chars
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
 
class Chars():
    """org.apache.logging.log4j.util.Chars"""
 
    @staticmethod
    def __wrap(java_value: __Chars) -> 'Chars':
        return Chars(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Chars):
        """
        Dynamic initializer for Chars.
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

    @staticmethod
    @overload
    def getLowerCaseHex(digit: int) -> str:
        """public static char org.apache.logging.log4j.util.Chars.getLowerCaseHex(int)"""
        return str.__wrap(__Chars.getLowerCaseHex(__int.valueOf(digit)))

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

    @staticmethod
    @overload
    def getUpperCaseHex(digit: int) -> str:
        """public static char org.apache.logging.log4j.util.Chars.getUpperCaseHex(int)"""
        return str.__wrap(__Chars.getUpperCaseHex(__int.valueOf(digit))) 
 
 
# CLASS: org.apache.logging.log4j.util.StringMap
import org.apache.logging.log4j.util.StringMap as __StringMap
__StringMap = __StringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as __ReadOnlyStringMap
__ReadOnlyStringMap = __ReadOnlyStringMap
 
class StringMap(ABC):
    """org.apache.logging.log4j.util.StringMap"""
 
    @staticmethod
    def __wrap(java_value: __StringMap) -> 'StringMap':
        return StringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringMap):
        """
        Dynamic initializer for StringMap.
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
    def hashCode(self, ):
        """public abstract int org.apache.logging.log4j.util.StringMap.hashCode()"""
        pass

    @abstractmethod
    def freeze(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.freeze()"""
        pass

    @abstractmethod
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public abstract void org.apache.logging.log4j.util.StringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.clear()"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract void org.apache.logging.log4j.util.StringMap.putValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.util.StringMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def isFrozen(self, ):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.isFrozen()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.MessageSupplier
import org.apache.logging.log4j.util.MessageSupplier as __MessageSupplier
__MessageSupplier = __MessageSupplier
from abc import abstractmethod, ABC
 
class MessageSupplier(ABC):
    """org.apache.logging.log4j.util.MessageSupplier"""
 
    @staticmethod
    def __wrap(java_value: __MessageSupplier) -> 'MessageSupplier':
        return MessageSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageSupplier):
        """
        Dynamic initializer for MessageSupplier.
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
    def get(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.MessageSupplier.get()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable
import org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable as __MultiFormatStringBuilderFormattable
__MultiFormatStringBuilderFormattable = __MultiFormatStringBuilderFormattable
from builtins import str
import org.apache.logging.log4j.util.StringBuilderFormattable as __StringBuilderFormattable
__StringBuilderFormattable = __StringBuilderFormattable
import org.apache.logging.log4j.message.MultiformatMessage as __MultiformatMessage
__MultiformatMessage = __MultiformatMessage
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class MultiFormatStringBuilderFormattable(ABC):
    """org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable"""
 
    @staticmethod
    def __wrap(java_value: __MultiFormatStringBuilderFormattable) -> 'MultiFormatStringBuilderFormattable':
        return MultiFormatStringBuilderFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiFormatStringBuilderFormattable):
        """
        Dynamic initializer for MultiFormatStringBuilderFormattable.
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
    def getFormats(self, ):
        """public abstract java.lang.String[] org.apache.logging.log4j.message.MultiformatMessage.getFormats()"""
        pass

    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        pass

    @abstractmethod
    def getFormattedMessage(self, formats: 'String'):
        """public abstract java.lang.String org.apache.logging.log4j.message.MultiformatMessage.getFormattedMessage(java.lang.String[])"""
        pass

    @abstractmethod
    def formatTo(self, buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.StringBuilderFormattable.formatTo(java.lang.StringBuilder)"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.InternalApi
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.apache.logging.log4j.util.InternalApi as __InternalApi
__InternalApi = __InternalApi
from abc import abstractmethod, ABC
 
class InternalApi(ABC):
    """org.apache.logging.log4j.util.InternalApi"""
 
    @staticmethod
    def __wrap(java_value: __InternalApi) -> 'InternalApi':
        return InternalApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InternalApi):
        """
        Dynamic initializer for InternalApi.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.StringBuilderFormattable
import org.apache.logging.log4j.util.StringBuilderFormattable as __StringBuilderFormattable
__StringBuilderFormattable = __StringBuilderFormattable
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
 
class StringBuilderFormattable(ABC):
    """org.apache.logging.log4j.util.StringBuilderFormattable"""
 
    @staticmethod
    def __wrap(java_value: __StringBuilderFormattable) -> 'StringBuilderFormattable':
        return StringBuilderFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringBuilderFormattable):
        """
        Dynamic initializer for StringBuilderFormattable.
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
    def formatTo(self, buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.StringBuilderFormattable.formatTo(java.lang.StringBuilder)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.OsgiServiceLocator
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.apache.logging.log4j.util.OsgiServiceLocator as __OsgiServiceLocator
__OsgiServiceLocator = __OsgiServiceLocator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
import java.lang.invoke.MethodHandles.Lookup as Lookup
from builtins import int
 
class OsgiServiceLocator():
    """org.apache.logging.log4j.util.OsgiServiceLocator"""
 
    @staticmethod
    def __wrap(java_value: __OsgiServiceLocator) -> 'OsgiServiceLocator':
        return OsgiServiceLocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OsgiServiceLocator):
        """
        Dynamic initializer for OsgiServiceLocator.
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
        """public org.apache.logging.log4j.util.OsgiServiceLocator()"""
        val = __OsgiServiceLocator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup') -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.OsgiServiceLocator.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup)"""
        return Stream.__wrap(__OsgiServiceLocator.loadServices(serviceType, lookup))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup', verbose: bool) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.OsgiServiceLocator.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup,boolean)"""
        return Stream.__wrap(__OsgiServiceLocator.loadServices(serviceType, lookup, __boolean.valueOf(verbose)))

    @staticmethod
    @overload
    def isAvailable() -> bool:
        """public static boolean org.apache.logging.log4j.util.OsgiServiceLocator.isAvailable()"""
        return bool.__wrap(__OsgiServiceLocator.isAvailable())

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
    def __init__(self, ):
        """public org.apache.logging.log4j.util.OsgiServiceLocator()"""
        val = __OsgiServiceLocator()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.util.StringBuilders
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map.Entry as Entry
import java.lang.Long as __long
import java.lang.StringBuilder as __StringBuilder
__StringBuilder = __StringBuilder
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import org.apache.logging.log4j.util.StringBuilders as __StringBuilders
__StringBuilders = __StringBuilders
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StringBuilders():
    """org.apache.logging.log4j.util.StringBuilders"""
 
    @staticmethod
    def __wrap(java_value: __StringBuilders) -> 'StringBuilders':
        return StringBuilders(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringBuilders):
        """
        Dynamic initializer for StringBuilders.
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
 
    @staticmethod
    @overload
    def equalsIgnoreCase(left: 'CharSequence', leftOffset: int, leftLength: int, right: 'CharSequence', rightOffset: int, rightLength: int) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.equalsIgnoreCase(java.lang.CharSequence,int,int,java.lang.CharSequence,int,int)"""
        return bool.__wrap(__StringBuilders.equalsIgnoreCase(left, __int.valueOf(leftOffset), __int.valueOf(leftLength), right, __int.valueOf(rightOffset), __int.valueOf(rightLength)))

    @staticmethod
    @overload
    def appendValue(stringBuilder: 'StringBuilder', obj: object):
        """public static void org.apache.logging.log4j.util.StringBuilders.appendValue(java.lang.StringBuilder,java.lang.Object)"""
        __StringBuilders.appendValue(stringBuilder, obj)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def escapeJson(toAppendTo: 'StringBuilder', start: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.escapeJson(java.lang.StringBuilder,int)"""
        __StringBuilders.escapeJson(toAppendTo, __int.valueOf(start))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def escapeXml(toAppendTo: 'StringBuilder', start: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.escapeXml(java.lang.StringBuilder,int)"""
        __StringBuilders.escapeXml(toAppendTo, __int.valueOf(start))

    @staticmethod
    @overload
    def appendDqValue(sb: 'StringBuilder', value: object) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendDqValue(java.lang.StringBuilder,java.lang.Object)"""
        return StringBuilder.__wrap(__StringBuilders.appendDqValue(sb, value))

    @staticmethod
    @overload
    def equals(left: 'CharSequence', leftOffset: int, leftLength: int, right: 'CharSequence', rightOffset: int, rightLength: int) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.equals(java.lang.CharSequence,int,int,java.lang.CharSequence,int,int)"""
        return bool.__wrap(__StringBuilders.equals(left, __int.valueOf(leftOffset), __int.valueOf(leftLength), right, __int.valueOf(rightOffset), __int.valueOf(rightLength)))

    @staticmethod
    @overload
    def appendKeyDqValue(sb: 'StringBuilder', key: str, value: object) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendKeyDqValue(java.lang.StringBuilder,java.lang.String,java.lang.Object)"""
        return StringBuilder.__wrap(__StringBuilders.appendKeyDqValue(sb, key, value))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def appendSpecificTypes(stringBuilder: 'StringBuilder', obj: object) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.appendSpecificTypes(java.lang.StringBuilder,java.lang.Object)"""
        return bool.__wrap(__StringBuilders.appendSpecificTypes(stringBuilder, obj))

    @staticmethod
    @overload
    def appendKeyDqValue(sb: 'StringBuilder', entry: 'Entry') -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendKeyDqValue(java.lang.StringBuilder,java.util.Map$Entry<java.lang.String, java.lang.String>)"""
        return StringBuilder.__wrap(__StringBuilders.appendKeyDqValue(sb, entry))

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

    @staticmethod
    @overload
    def trimToMaxSize(stringBuilder: 'StringBuilder', maxSize: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.trimToMaxSize(java.lang.StringBuilder,int)"""
        __StringBuilders.trimToMaxSize(stringBuilder, __int.valueOf(maxSize))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))