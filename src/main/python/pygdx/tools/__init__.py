from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.tools.FileProcessor as __FileProcessor_Entry
__Entry = __FileProcessor_Entry.Entry
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.tools.FileProcessor.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = __Entry()
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.FileProcessor$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'File', arg1: 'File'):
        """public com.badlogic.gdx.tools.FileProcessor$Entry(java.io.File,java.io.File)"""
        val = __Entry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor$Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.tools.FileProcessor as __FileProcessor_Entry
__Entry = __FileProcessor_Entry.Entry
from builtins import bool
from builtins import int
 
class Entry():
    """com.badlogic.gdx.tools.FileProcessor.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = __Entry()
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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.FileProcessor$Entry.toString()"""
        return str.__wrap(super(Entry, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = __Entry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'File', arg1: 'File'):
        """public com.badlogic.gdx.tools.FileProcessor$Entry(java.io.File,java.io.File)"""
        val = __Entry(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor$Entry 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.FileProcessor as __FileProcessor
__FileProcessor = __FileProcessor
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.FilenameFilter as FilenameFilter
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FileProcessor():
    """com.badlogic.gdx.tools.FileProcessor"""
 
    @staticmethod
    def __wrap(java_value: __FileProcessor) -> 'FileProcessor':
        return FileProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileProcessor):
        """
        Dynamic initializer for FileProcessor.
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
    def process(self, arg0: str, arg1: str) -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.lang.String,java.lang.String) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__FileProcessor, self).process(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setFlattenOutput(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setFlattenOutput(boolean)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).setFlattenOutput(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'FileProcessor'):
        """public com.badlogic.gdx.tools.FileProcessor(com.badlogic.gdx.tools.FileProcessor)"""
        val = __FileProcessor(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addInputRegex(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputRegex(java.lang.String...)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).addInputRegex(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = __FileProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setOutputSuffix(self, arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setOutputSuffix(java.lang.String)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).setOutputSuffix(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = __FileProcessor()
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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File,java.io.File) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__FileProcessor, self).process(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setComparator(self, arg0: 'Comparator') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setComparator(java.util.Comparator<java.io.File>)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).setComparator(arg0))

    @overload
    def setRecursive(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setRecursive(boolean)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).setRecursive(__boolean.valueOf(arg0)))

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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File[],java.io.File) throws java.lang.Exception"""
        return 'ArrayList'.__wrap(super(__FileProcessor, self).process(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addInputSuffix(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputSuffix(java.lang.String...)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).addInputSuffix(arg0))

    @overload
    def setInputFilter(self, arg0: 'FilenameFilter') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setInputFilter(java.io.FilenameFilter)"""
        return 'FileProcessor'.__wrap(super(__FileProcessor, self).setInputFilter(arg0))