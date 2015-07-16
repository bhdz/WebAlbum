'''
Created on Jul 16, 2015

@author: dakkar
'''
import inspect
from pulo import Labeled # Fur zie Futuresz, Magnum Opus Lib for Python Trqq se maznia na ed1n p1chaga
# 
# Meta-class? Yes.
#This gathers info about something and so on
class CallableI(dict): # Metaclass
    
    def __init__(self, Methf_, Arg_types = [], Kws_types = {}, **options):
        self._Type = {}
        if 'Type' in options:
            self._Type = options.pop('Type')
        self._Type = self.__call__(Methf_, *Arg_types, **Kws_types)
    
    #
    # This is getting Dicty by default.. sorry no time to be eloquent
    #&3 not now... needsz Expansion
    #
    def _pop(self, Name, Second = None, **opts):
        pass
    
    # Sorry for the state of this. I am ina rush
    # This is getting Cally by default, needs mixage
    # FMeth is either a function object or a Method and Self tuple 
    # => if isinstance(F, tuple) => Pass a tuple for Function and Self
    # => or else _make_call starts inspect(F)ing
    # => This is Info meta-class idea
    def _make_call(self, F = (None, None), *args, **keywords):
        """ Meta :: Perform_call on Arguments on already gathered info"""
        Method_ = None
        Function_ = None
        First = None
        Rest = args
        Keys = keywords
        Callable = Function_
        
        if self.calling_method:
            First = args.pop(0)
            Rest = args
            Callable = self._get('Method')
            
        elif self.calling_function:
            Callable = self._get('Function')
            Rest
        else:
            Callable = Function_
            
        State_ = self._pop('State', None)
        
        if self.calling_method:
            Result = Callable(First, *Rest, **Keys)
        elif self.calling_function:
            Result = Callable( First, *Rest )
        else:
            Result = Callable(*Rest, **Keys)
        return Result
        # BAD THIKNING
        
    @property
    def calling_method(self):
        return True # TrueOrFalsehood 
    
    @property
    def calling_function(self):
        return True # TrueOrFalse-hood
    
    def __call__(self, InspectionSubj, *ArgsType, **KwTypes):
        return inspect.isfunction(InspectionSubj)

# Interface Base
#
class Func(CallableI):
    def __init__(self, target, 
                 ArgsTypesExpected = [], KeysTypesExpected = {}, 
                 *args_inspect, **options):
        
        pass
    def __call__(self, *args, ):
        pass
#
# This is a Decorator, not a Pattern
#&shamelessplug.3 Phuture: f._state['$'][_{{is_function,returns,values}}]
#
def memoized(f,*args, **options):
    
    f._is_function = inspect.isfunction(f)
    f._returns = { ([],{}): False }
    f._values = { ([],{}): [] }
    
    # This is for the future, Pattern def Memoized
    f._plug = {}


    def _called(*args, **keys):
        try:
            if f._is_function:
                Result = f(*args, **keys)
            else:
                first = args.pop(0)
                rest = args
                Result = f(first, *rest, **keys)
            
            # Caching part goes here @_@
            f._returns[ (Result, f) ] = True
            f._values[ (Result, f) ].append(Result)
        except KeyError, err:
            raise err # Hell
         
    def _cache(thang = (None, None), *thangs, **opts):
        return f._values
    
    def _cached(thang1 = (None, None), *arguments):
        ret = None
        # Check in the standart 
        try:
            value_listage = f._values[thang1]
            if not ret in value_listage:
                ret = None # dunno what to do at this point
                raise ValueError("ret=%s" % ret)
        except KeyError:
            ret = None # dunno what to do at this point
        return ret
    
    def inner(*args, **keys):
        ret = None
        try:
            if _cached( (args, keys) ):
                ret = _cache( (args, keys) )
            else:
                ret = _called(*args, **keys)
        except:
            ret = None
        return ret
    return inner

# 
# This is a Pattern-ed, decoration
# Remove this class Single hierarchy Inheritance and Mixin Pattern
#
class Memoize(object, dict):
    pass

#
# This is just for kicks and giggles, I am outta job ahahahah
#
def Memoized(Subject_ = None, *args, **keys):
    def inner_object(SomeThing, *Rest, **KeysContext):
        pass
    
    def inner_(*args, **keys):
        return Func(Subject_).results
    
    return inner_

# this is the middle grounds
# The fun and What_ must be Adapted(interface1, interface2) -> adapted(instance1, instance2) -> _results?yes.
# 
def wrapf(f, before_f, after_f, what_ = None, **options): # 
    f._is_function = inspect.isfunction(f)
    f._methf = f
    f._what = what_
    
    def _caller(*args, **keys):
        pass
    
    def _results(arg):
        pass
    
    def after(*args, **keys):
        pass
    
    def before(*args, **keys):
        pass
    
    f.after = after
    f.results = _results
    f.calling = f
    
    def inner_call(*args, **keys):
        f.before(*args, **keys)
        f.results = f.calling(*args, **keys)
        f.after(*args, **keys)
        return _results(f, f.results)
    return inner_call
