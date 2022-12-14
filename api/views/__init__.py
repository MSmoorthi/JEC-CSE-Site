from .views import index, get_choices
from .student import StudentModelViewSet, StudentBatchView
from .staff import StaffModelViewSet, StaffAchievementModelViewSet
from .alumni import (
    AlumniListView,
    AlumniDetailView,
    AlumniWorkModelViewSet,
    AlumniWorkMultivaluedView,
)
from .event import (
    EventPhotoModelViewSet,
    EventVideoModelViewSet,
    EventWinnerModelViewSet,
    EventModelViewSet,
    EventListView,
    EventDetailView,
    EventPhotosMultivaluedView,
    EventVideosMultivaluedView,
)
from .infrastructure import (
    InfrastructureModelViewSet,
    InfrastructureImagesModelViewSet,
)
from .academic_council import AcademicCouncilViewSet, AcademicCouncilMeetingViewSet
from .student_achievement import StudentAchievementModelViewSet
from .project import ProjectModelViewSet
from .subject import SubjectModelViewSet
