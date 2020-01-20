""" import c functions from <launch.h> """

import ctypes

__libSystem__ = ctypes.CDLL("/usr/lib/libSystem.dylib")

LAUNCH_KEY_SUBMITJOB = "SubmitJob"
LAUNCH_KEY_REMOVEJOB = "RemoveJob"
LAUNCH_KEY_STARTJOB = "StartJob"
LAUNCH_KEY_STOPJOB = "StopJob"
LAUNCH_KEY_GETJOB = "GetJob"
LAUNCH_KEY_GETJOBS = "GetJobs"
LAUNCH_KEY_CHECKIN = "CheckIn"

LAUNCH_JOBKEY_LABEL = "Label"
LAUNCH_JOBKEY_DISABLED = "Disabled"
LAUNCH_JOBKEY_USERNAME = "UserName"
LAUNCH_JOBKEY_GROUPNAME = "GroupName"
LAUNCH_JOBKEY_TIMEOUT = "TimeOut"
LAUNCH_JOBKEY_EXITTIMEOUT = "ExitTimeOut"
LAUNCH_JOBKEY_INITGROUPS = "InitGroups"
LAUNCH_JOBKEY_SOCKETS = "Sockets"
LAUNCH_JOBKEY_MACHSERVICES = "MachServices"
LAUNCH_JOBKEY_MACHSERVICELOOKUPPOLICIES = "MachServiceLookupPolicies"
LAUNCH_JOBKEY_INETDCOMPATIBILITY = "inetdCompatibility"
LAUNCH_JOBKEY_ENABLEGLOBBING = "EnableGlobbing"
LAUNCH_JOBKEY_PROGRAMARGUMENTS = "ProgramArguments"
LAUNCH_JOBKEY_PROGRAM = "Program"
LAUNCH_JOBKEY_ONDEMAND = "OnDemand"
LAUNCH_JOBKEY_KEEPALIVE = "KeepAlive"
LAUNCH_JOBKEY_LIMITLOADTOHOSTS = "LimitLoadToHosts"
LAUNCH_JOBKEY_LIMITLOADFROMHOSTS = "LimitLoadFromHosts"
LAUNCH_JOBKEY_LIMITLOADTOSESSIONTYPE = "LimitLoadToSessionType"
LAUNCH_JOBKEY_LIMITLOADTOHARDWARE = "LimitLoadToHardware"
LAUNCH_JOBKEY_LIMITLOADFROMHARDWARE = "LimitLoadFromHardware"
LAUNCH_JOBKEY_RUNATLOAD = "RunAtLoad"
LAUNCH_JOBKEY_ROOTDIRECTORY = "RootDirectory"
LAUNCH_JOBKEY_WORKINGDIRECTORY = "WorkingDirectory"
LAUNCH_JOBKEY_ENVIRONMENTVARIABLES = "EnvironmentVariables"
LAUNCH_JOBKEY_USERENVIRONMENTVARIABLES = "UserEnvironmentVariables"
LAUNCH_JOBKEY_UMASK = "Umask"
LAUNCH_JOBKEY_NICE = "Nice"
LAUNCH_JOBKEY_HOPEFULLYEXITSFIRST = "HopefullyExitsFirst"
LAUNCH_JOBKEY_HOPEFULLYEXITSLAST = "HopefullyExitsLast"
LAUNCH_JOBKEY_LOWPRIORITYIO = "LowPriorityIO"
LAUNCH_JOBKEY_LOWPRIORITYBACKGROUNDIO = "LowPriorityBackgroundIO"
LAUNCH_JOBKEY_MATERIALIZEDATALESSFILES = "MaterializeDatalessFiles"
LAUNCH_JOBKEY_SESSIONCREATE = "SessionCreate"
LAUNCH_JOBKEY_STARTONMOUNT = "StartOnMount"
LAUNCH_JOBKEY_SOFTRESOURCELIMITS = "SoftResourceLimits"
LAUNCH_JOBKEY_HARDRESOURCELIMITS = "HardResourceLimits"
LAUNCH_JOBKEY_STANDARDINPATH = "StandardInPath"
LAUNCH_JOBKEY_STANDARDOUTPATH = "StandardOutPath"
LAUNCH_JOBKEY_STANDARDERRORPATH = "StandardErrorPath"
LAUNCH_JOBKEY_DEBUG = "Debug"
LAUNCH_JOBKEY_WAITFORDEBUGGER = "WaitForDebugger"
LAUNCH_JOBKEY_QUEUEDIRECTORIES = "QueueDirectories"
LAUNCH_JOBKEY_HOMERELATIVEQUEUEDIRECTORIES = "HomeRelativeQueueDirectories"
LAUNCH_JOBKEY_WATCHPATHS = "WatchPaths"
LAUNCH_JOBKEY_STARTINTERVAL = "StartInterval"
LAUNCH_JOBKEY_STARTCALENDARINTERVAL = "StartCalendarInterval"
LAUNCH_JOBKEY_BONJOURFDS = "BonjourFDs"
LAUNCH_JOBKEY_LASTEXITSTATUS = "LastExitStatus"
LAUNCH_JOBKEY_PID = "PID"
LAUNCH_JOBKEY_THROTTLEINTERVAL = "ThrottleInterval"
LAUNCH_JOBKEY_LAUNCHONLYONCE = "LaunchOnlyOnce"
LAUNCH_JOBKEY_ABANDONPROCESSGROUP = "AbandonProcessGroup"
LAUNCH_JOBKEY_IGNOREPROCESSGROUPATSHUTDOWN = "IgnoreProcessGroupAtShutdown"
LAUNCH_JOBKEY_LEGACYTIMERS = "LegacyTimers"
LAUNCH_JOBKEY_ENABLEPRESSUREDEXIT = "EnablePressuredExit"
LAUNCH_JOBKEY_ENABLETRANSACTIONS = "EnableTransactions"
LAUNCH_JOBKEY_DRAINMESSAGESONFAILEDINIT = "DrainMessagesOnFailedInit"
LAUNCH_JOBKEY_POLICIES = "Policies"

LAUNCH_JOBKEY_PUBLISHESEVENTS = "PublishesEvents"
LAUNCH_KEY_PUBLISHESEVENTS_DOMAININTERNAL = "DomainInternal"

LAUNCH_JOBPOLICY_DENYCREATINGOTHERJOBS = "DenyCreatingOtherJobs"

LAUNCH_JOBINETDCOMPATIBILITY_WAIT = "Wait"
LAUNCH_JOBINETDCOMPATIBILITY_INSTANCES = "Instances"

LAUNCH_JOBKEY_MACH_RESETATCLOSE = "ResetAtClose"
LAUNCH_JOBKEY_MACH_HIDEUNTILCHECKIN = "HideUntilCheckIn"

LAUNCH_JOBKEY_KEEPALIVE_SUCCESSFULEXIT = "SuccessfulExit"
LAUNCH_JOBKEY_KEEPALIVE_NETWORKSTATE = "NetworkState"
LAUNCH_JOBKEY_KEEPALIVE_PATHSTATE = "PathState"
LAUNCH_JOBKEY_KEEPALIVE_HOMERELATIVEPATHSTATE = "HomeRelativePathState"
LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBACTIVE = "OtherJobActive"
LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBENABLED = "OtherJobEnabled"
LAUNCH_JOBKEY_KEEPALIVE_AFTERINITIALDEMAND = "AfterInitialDemand"
LAUNCH_JOBKEY_KEEPALIVE_CRASHED = "Crashed"

LAUNCH_JOBKEY_LAUNCHEVENTS = "LaunchEvents"

LAUNCH_JOBKEY_CAL_MINUTE = "Minute"
LAUNCH_JOBKEY_CAL_HOUR = "Hour"
LAUNCH_JOBKEY_CAL_DAY = "Day"
LAUNCH_JOBKEY_CAL_WEEKDAY = "Weekday"
LAUNCH_JOBKEY_CAL_MONTH = "Month"

LAUNCH_JOBKEY_RESOURCELIMIT_CORE = "Core"
LAUNCH_JOBKEY_RESOURCELIMIT_CPU = "CPU"
LAUNCH_JOBKEY_RESOURCELIMIT_DATA = "Data"
LAUNCH_JOBKEY_RESOURCELIMIT_FSIZE = "FileSize"
LAUNCH_JOBKEY_RESOURCELIMIT_MEMLOCK = "MemoryLock"
LAUNCH_JOBKEY_RESOURCELIMIT_NOFILE = "NumberOfFiles"
LAUNCH_JOBKEY_RESOURCELIMIT_NPROC = "NumberOfProcesses"
LAUNCH_JOBKEY_RESOURCELIMIT_RSS = "ResidentSetSize"
LAUNCH_JOBKEY_RESOURCELIMIT_STACK = "Stack"

LAUNCH_JOBKEY_DISABLED_MACHINETYPE = "MachineType"
LAUNCH_JOBKEY_DISABLED_MODELNAME = "ModelName"

LAUNCH_JOBKEY_DATASTORES = "Datastores"
LAUNCH_JOBKEY_DATASTORES_SIZELIMIT = "SizeLimit"

LAUNCH_JOBSOCKETKEY_TYPE = "SockType"
LAUNCH_JOBSOCKETKEY_PASSIVE = "SockPassive"
LAUNCH_JOBSOCKETKEY_BONJOUR = "Bonjour"
LAUNCH_JOBSOCKETKEY_SECUREWITHKEY = "SecureSocketWithKey"
LAUNCH_JOBSOCKETKEY_PATHNAME = "SockPathName"
LAUNCH_JOBSOCKETKEY_PATHMODE = "SockPathMode"
LAUNCH_JOBSOCKETKEY_PATHOWNER = "SockPathOwner"
LAUNCH_JOBSOCKETKEY_PATHGROUP = "SockPathGroup"
LAUNCH_JOBSOCKETKEY_NODENAME = "SockNodeName"
LAUNCH_JOBSOCKETKEY_SERVICENAME = "SockServiceName"
LAUNCH_JOBSOCKETKEY_FAMILY = "SockFamily"
LAUNCH_JOBSOCKETKEY_PROTOCOL = "SockProtocol"
LAUNCH_JOBSOCKETKEY_MULTICASTGROUP = "MulticastGroup"

LAUNCH_JOBKEY_PROCESSTYPE = "ProcessType"
LAUNCH_KEY_PROCESSTYPE_APP = "App"
LAUNCH_KEY_PROCESSTYPE_STANDARD = "Standard"
LAUNCH_KEY_PROCESSTYPE_BACKGROUND = "Background"
LAUNCH_KEY_PROCESSTYPE_INTERACTIVE = "Interactive"
LAUNCH_KEY_PROCESSTYPE_ADAPTIVE = "Adaptive"

""" typedef enum launch_data_type_t """
LAUNCH_DATA_DICTIONARY = 1
LAUNCH_DATA_ARRAY = 2
LAUNCH_DATA_FD = 3
LAUNCH_DATA_INTEGER = 4
LAUNCH_DATA_REAL = 5
LAUNCH_DATA_BOOL = 6
LAUNCH_DATA_STRING = 7
LAUNCH_DATA_OPAQUE = 8
LAUNCH_DATA_ERRNO = 9
LAUNCH_DATA_MACHPORT = 10

""" int launch_activate_socket(const char *name, int * _Nonnull * _Nullable fds, size_t *cnt); """
launch_activate_socket = __libSystem__.launch_activate_socket
launch_activate_socket.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.POINTER(ctypes.c_size_t)]
launch_activate_socket.restype = ctypes.c_int

""" typedef void (*launch_data_dict_iterator_t)(const launch_data_t lval, const char *key, void * _Nullable ctx); """
launch_data_dict_iterator_t = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)

""" launch_data_t launch_data_alloc(launch_data_type_t type); """
launch_data_alloc = __libSystem__.launch_data_alloc
launch_data_alloc.argtypes = [ctypes.c_uint]
launch_data_alloc.restype = ctypes.c_void_p

""" launch_data_t launch_data_copy(launch_data_t ld); """
launch_data_copy = __libSystem__.launch_data_copy
launch_data_copy.argtypes = [ctypes.c_void_p]
launch_data_copy.restype = ctypes.c_void_p

""" launch_data_type_t launch_data_get_type(const launch_data_t ld); """
launch_data_get_type = __libSystem__.launch_data_get_type
launch_data_get_type.argtypes = [ctypes.c_void_p]
launch_data_get_type.restype = ctypes.c_uint

""" void launch_data_free(launch_data_t ld); """
launch_data_free = __libSystem__.launch_data_free
launch_data_free.argtypes = [ctypes.c_void_p]
launch_data_free.restype = None

""" bool launch_data_dict_insert(launch_data_t ldict, const launch_data_t lval, const char *key); """
launch_data_dict_insert = __libSystem__.launch_data_dict_insert
launch_data_dict_insert.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
launch_data_dict_insert.restype = ctypes.c_bool

""" launch_data_t _Nullable launch_data_dict_lookup(const launch_data_t ldict, const char *key); """
launch_data_dict_lookup = __libSystem__.launch_data_dict_lookup
launch_data_dict_lookup.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
launch_data_dict_lookup.restype = ctypes.c_void_p

""" bool launch_data_dict_remove(launch_data_t ldict, const char *key); """
launch_data_dict_remove = __libSystem__.launch_data_dict_remove
launch_data_dict_remove.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
launch_data_dict_remove.restype = ctypes.c_bool

""" void launch_data_dict_iterate(const launch_data_t ldict, launch_data_dict_iterator_t iterator, void * _Nullable ctx); """
launch_data_dict_iterate = __libSystem__.launch_data_dict_iterate
launch_data_dict_iterate.argtypes = [ctypes.c_void_p, launch_data_dict_iterator_t, ctypes.c_void_p]
launch_data_dict_iterate.restype = None

""" size_t launch_data_dict_get_count(const launch_data_t ldict); """
launch_data_dict_get_count = __libSystem__.launch_data_dict_get_count
launch_data_dict_get_count.argtypes = [ctypes.c_void_p]
launch_data_dict_get_count.restype = ctypes.c_size_t

""" bool launch_data_array_set_index(launch_data_t larray, const launch_data_t lval, size_t idx); """
launch_data_array_set_index = __libSystem__.launch_data_array_set_index
launch_data_array_set_index.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
launch_data_array_set_index.restype = ctypes.c_bool

""" launch_data_t launch_data_array_get_index(const launch_data_t larray, size_t idx); """
launch_data_array_get_index = __libSystem__.launch_data_array_get_index
launch_data_array_get_index.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
launch_data_array_get_index.restype = ctypes.c_void_p

""" size_t launch_data_array_get_count(const launch_data_t larray); """
launch_data_array_get_count = __libSystem__.launch_data_array_get_count
launch_data_array_get_count.argtypes = [ctypes.c_void_p]
launch_data_array_get_count.restype = ctypes.c_size_t

""" launch_data_t launch_data_new_fd(int fd); """
launch_data_new_fd = __libSystem__.launch_data_new_fd
launch_data_new_fd.argtypes = [ctypes.c_int]
launch_data_new_fd.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_machport(mach_port_t val); """
launch_data_new_machport = __libSystem__.launch_data_new_machport
launch_data_new_machport.argtypes = [ctypes.c_uint]
launch_data_new_machport.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_integer(long long val); """
launch_data_new_integer = __libSystem__.launch_data_new_integer
launch_data_new_integer.argtypes = [ctypes.c_longlong]
launch_data_new_integer.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_bool(bool val); """
launch_data_new_bool = __libSystem__.launch_data_new_bool
launch_data_new_bool.argtypes = [ctypes.c_bool]
launch_data_new_bool.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_real(double val); """
launch_data_new_real = __libSystem__.launch_data_new_real
launch_data_new_real.argtypes = [ctypes.c_double]
launch_data_new_real.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_string(const char *val); """
launch_data_new_string = __libSystem__.launch_data_new_string
launch_data_new_string.argtypes = [ctypes.c_char_p]
launch_data_new_string.restype = ctypes.c_void_p

""" launch_data_t launch_data_new_opaque(const void *bytes, size_t sz); """
launch_data_new_opaque = __libSystem__.launch_data_new_opaque
launch_data_new_opaque.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
launch_data_new_opaque.restype = ctypes.c_void_p

""" bool launch_data_set_fd(launch_data_t ld, int fd); """
launch_data_set_fd = __libSystem__.launch_data_set_fd
launch_data_set_fd.argtypes = [ctypes.c_void_p, ctypes.c_int]
launch_data_set_fd.restype = ctypes.c_bool

""" bool launch_data_set_machport(launch_data_t ld, mach_port_t mp); """
launch_data_set_machport = __libSystem__.launch_data_set_machport
launch_data_set_machport.argtypes = [ctypes.c_void_p, ctypes.c_uint]
launch_data_set_machport.restype = ctypes.c_bool

""" bool launch_data_set_integer(launch_data_t ld, long long val); """
launch_data_set_integer = __libSystem__.launch_data_set_integer
launch_data_set_integer.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
launch_data_set_integer.restype = ctypes.c_bool

""" bool launch_data_set_bool(launch_data_t ld, bool val); """
launch_data_set_bool = __libSystem__.launch_data_set_bool
launch_data_set_bool.argtypes = [ctypes.c_void_p, ctypes.c_bool]
launch_data_set_bool.restype = ctypes.c_bool

""" bool launch_data_set_real(launch_data_t ld, double val); """
launch_data_set_real = __libSystem__.launch_data_set_real
launch_data_set_real.argtypes = [ctypes.c_void_p, ctypes.c_double]
launch_data_set_real.restype = ctypes.c_bool

""" bool launch_data_set_string(launch_data_t ld, const char *val); """
launch_data_set_string = __libSystem__.launch_data_set_string
launch_data_set_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
launch_data_set_string.restype = ctypes.c_bool

""" bool launch_data_set_opaque(launch_data_t ld, const void *bytes, size_t sz); """
launch_data_set_opaque = __libSystem__.launch_data_set_opaque
launch_data_set_opaque.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
launch_data_set_opaque.restype = ctypes.c_bool

""" int launch_data_get_fd(const launch_data_t ld); """
launch_data_get_fd = __libSystem__.launch_data_get_fd
launch_data_get_fd.argtypes = [ctypes.c_void_p]
launch_data_get_fd.restype = ctypes.c_int

""" mach_port_t launch_data_get_machport(const launch_data_t ld); """
launch_data_get_machport = __libSystem__.launch_data_get_machport
launch_data_get_machport.argtypes = [ctypes.c_void_p]
launch_data_get_machport.restype = ctypes.c_uint

""" long long launch_data_get_integer(const launch_data_t ld); """
launch_data_get_integer = __libSystem__.launch_data_get_integer
launch_data_get_integer.argtypes = [ctypes.c_void_p]
launch_data_get_integer.restype = ctypes.c_longlong

""" bool launch_data_get_bool(const launch_data_t ld); """
launch_data_get_bool = __libSystem__.launch_data_get_bool
launch_data_get_bool.argtypes = [ctypes.c_void_p]
launch_data_get_bool.restype = ctypes.c_bool

""" double launch_data_get_real(const launch_data_t ld); """
launch_data_get_real = __libSystem__.launch_data_get_real
launch_data_get_real.argtypes = [ctypes.c_void_p]
launch_data_get_real.restype = ctypes.c_double

""" const char * launch_data_get_string(const launch_data_t ld); """
launch_data_get_string = __libSystem__.launch_data_get_string
launch_data_get_string.argtypes = [ctypes.c_void_p]
launch_data_get_string.restype = ctypes.c_char_p

""" void * launch_data_get_opaque(const launch_data_t ld); """
launch_data_get_opaque = __libSystem__.launch_data_get_opaque
launch_data_get_opaque.argtypes = [ctypes.c_void_p]
launch_data_get_opaque.restype = ctypes.c_void_p

""" int launch_data_get_errno(const launch_data_t ld); """
launch_data_get_errno = __libSystem__.launch_data_get_errno
launch_data_get_errno.argtypes = [ctypes.c_void_p]
launch_data_get_errno.restype = ctypes.c_int

""" int launch_get_fd(void); """
launch_get_fd = __libSystem__.launch_get_fd
launch_get_fd.argtypes = None
launch_get_fd.restype = ctypes.c_int

""" launch_data_t launch_msg(const launch_data_t request); """
launch_msg = __libSystem__.launch_msg
launch_msg.argtypes = [ctypes.c_void_p]
launch_msg.restype = ctypes.c_void_p
