from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.FileProcessor as _FileProcessor
_FileProcessor = _FileProcessor
import java.lang.String as _String
_String = _String
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileProcessor():
    """com.badlogic.gdx.tools.FileProcessor"""
 
    @staticmethod
    def _wrap(java_value: _FileProcessor) -> 'FileProcessor':
        return FileProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileProcessor):
        """
        Dynamic initializer for FileProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFlattenOutput(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setFlattenOutput(boolean)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setFlattenOutput(_boolean.valueOf(arg0)))

    @overload
    def setRecursive(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setRecursive(boolean)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setRecursive(_boolean.valueOf(arg0)))

    @overload
    def addInputSuffix(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputSuffix(java.lang.String...)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).addInputSuffix(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = _FileProcessor()
        self.__wrapper = val

    @overload
    def addInputRegex(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputRegex(java.lang.String...)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).addInputRegex(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOutputSuffix(self, arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setOutputSuffix(java.lang.String)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setOutputSuffix(arg0))

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

    @overload
    def setComparator(self, arg0: 'Comparator') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setComparator(java.util.Comparator<java.io.File>)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setComparator(arg0))

    @overload
    def setInputFilter(self, arg0: 'FilenameFilter') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setInputFilter(java.io.FilenameFilter)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setInputFilter(arg0))

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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File,java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @overload
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File[],java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = _FileProcessor()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileProcessor'):
        """public com.badlogic.gdx.tools.FileProcessor(com.badlogic.gdx.tools.FileProcessor)"""
        val = _FileProcessor(arg0)
        self.__wrapper = val

    @overload
    def process(self, arg0: str, arg1: str) -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.lang.String,java.lang.String) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.FileProcessor as _FileProcessor
_FileProcessor = _FileProcessor
import java.lang.String as _String
_String = _String
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import java.util.Comparator as Comparator
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileProcessor():
    """com.badlogic.gdx.tools.FileProcessor"""
 
    @staticmethod
    def _wrap(java_value: _FileProcessor) -> 'FileProcessor':
        return FileProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileProcessor):
        """
        Dynamic initializer for FileProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFlattenOutput(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setFlattenOutput(boolean)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setFlattenOutput(_boolean.valueOf(arg0)))

    @overload
    def setRecursive(self, arg0: bool) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setRecursive(boolean)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setRecursive(_boolean.valueOf(arg0)))

    @overload
    def addInputSuffix(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputSuffix(java.lang.String...)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).addInputSuffix(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = _FileProcessor()
        self.__wrapper = val

    @overload
    def addInputRegex(self, *arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.addInputRegex(java.lang.String...)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).addInputRegex(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOutputSuffix(self, arg0: str) -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setOutputSuffix(java.lang.String)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setOutputSuffix(arg0))

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

    @overload
    def setComparator(self, arg0: 'Comparator') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setComparator(java.util.Comparator<java.io.File>)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setComparator(arg0))

    @overload
    def setInputFilter(self, arg0: 'FilenameFilter') -> 'FileProcessor':
        """public com.badlogic.gdx.tools.FileProcessor com.badlogic.gdx.tools.FileProcessor.setInputFilter(java.io.FilenameFilter)"""
        return 'FileProcessor'._wrap(super(_FileProcessor, self).setInputFilter(arg0))

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
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File,java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @overload
    def process(self, arg0: 'File', arg1: 'File') -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.io.File[],java.io.File) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor()"""
        val = _FileProcessor()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileProcessor'):
        """public com.badlogic.gdx.tools.FileProcessor(com.badlogic.gdx.tools.FileProcessor)"""
        val = _FileProcessor(arg0)
        self.__wrapper = val

    @overload
    def process(self, arg0: str, arg1: str) -> 'ArrayList':
        """public java.util.ArrayList<com.badlogic.gdx.tools.FileProcessor$Entry> com.badlogic.gdx.tools.FileProcessor.process(java.lang.String,java.lang.String) throws java.lang.Exception"""
        return 'ArrayList'._wrap(super(_FileProcessor, self).process(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor 
 
 
# CLASS: com.badlogic.gdx.tools.FileProcessor$Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.tools.FileProcessor as _FileProcessor_Entry
_Entry = _FileProcessor_Entry.Entry
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Entry():
    """com.badlogic.gdx.tools.FileProcessor.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = _Entry()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'File', arg1: 'File'):
        """public com.badlogic.gdx.tools.FileProcessor$Entry(java.io.File,java.io.File)"""
        val = _Entry(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.FileProcessor$Entry.toString()"""
        return str._wrap(super(Entry, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.FileProcessor$Entry()"""
        val = _Entry()
        self.__wrapper = val