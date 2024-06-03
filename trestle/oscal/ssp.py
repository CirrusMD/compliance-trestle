# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
#
####### DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT ######
#                                                                        #
#        This file is automatically generated by gen_oscal.py            #
#                                                                        #
####### DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT DO NOT EDIT ######
#
#
from __future__ import annotations

import re
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic.v1 import AnyUrl, EmailStr, Extra, Field, conint, constr, validator

from trestle.core.base_model import OscalBaseModel
from trestle.oscal import OSCAL_VERSION_REGEX, OSCAL_VERSION
import trestle.oscal.common as common
from trestle.oscal.common import Status, SystemComponent


class AdjustmentJustification(OscalBaseModel):
    __root__: str = Field(
        ...,
        description=
        'If the selected security level is different from the base security level, this contains the justification for the change.',
        title='Adjustment Justification'
    )


class System(Enum):
    """
    Specifies the information type identification system used.
    """

    http___doi_org_10_6028_NIST_SP_800_60v2r1 = 'http://doi.org/10.6028/NIST.SP.800-60v2r1'


class SetParameter(OscalBaseModel):
    """
    Identifies the parameter that will be set by the enclosed value.
    """

    class Config:
        extra = Extra.forbid

    param_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='param-id',
        description=
        "A human-oriented reference to a parameter within a control, who's catalog has been imported into the current implementation context.",
        title='Parameter ID'
    )
    values: List[constr(regex=r'^\S(.*\S)?$')] = Field(...)
    remarks: Optional[str] = None


class Selected(OscalBaseModel):
    __root__: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        description='The selected (Confidentiality, Integrity, or Availability) security impact level.',
        title='Selected Level (Confidentiality, Integrity, or Availability)'
    )


class SecurityImpactLevel(OscalBaseModel):
    """
    The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
    """

    class Config:
        extra = Extra.forbid

    security_objective_confidentiality: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        alias='security-objective-confidentiality',
        description=
        'A target-level of confidentiality for the system, based on the sensitivity of information within the system.',
        title='Security Objective: Confidentiality'
    )
    security_objective_integrity: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        alias='security-objective-integrity',
        description=
        'A target-level of integrity for the system, based on the sensitivity of information within the system.',
        title='Security Objective: Integrity'
    )
    security_objective_availability: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        alias='security-objective-availability',
        description=
        'A target-level of availability for the system, based on the sensitivity of information within the system.',
        title='Security Objective: Availability'
    )


class Satisfied(OscalBaseModel):
    """
    Describes how this system satisfies a responsibility imposed by a leveraged system.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this satisfied control implementation entry elsewhere in this or other OSCAL instances. The locally defined UUID of the control implementation can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Satisfied Universally Unique Identifier',
    )
    responsibility_uuid: Optional[constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )] = Field(
        None,
        alias='responsibility-uuid',
        description=
        'A machine-oriented identifier reference to a control implementation that satisfies a responsibility imposed by a leveraged system.',
        title='Responsibility UUID'
    )
    description: str = Field(
        ...,
        description=
        'An implementation statement that describes the aspects of a control or control statement implementation that a leveraging system is implementing based on a requirement from a leveraged system.',
        title='Satisfied Control Implementation Responsibility Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    remarks: Optional[str] = None


class Responsibility(OscalBaseModel):
    """
    Describes a control implementation responsibility imposed on a leveraging system.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this responsibility elsewhere in this or other OSCAL instances. The locally defined UUID of the responsibility can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Responsibility Universally Unique Identifier',
    )
    provided_uuid: Optional[constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )] = Field(
        None,
        alias='provided-uuid',
        description=
        'A machine-oriented identifier reference to an inherited control implementation that a leveraging system is inheriting from a leveraged system.',
        title='Provided UUID'
    )
    description: str = Field(
        ...,
        description=
        'An implementation statement that describes the aspects of the control or control statement implementation that a leveraging system must implement to satisfy the control provided by a leveraged system.',
        title='Control Implementation Responsibility Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    remarks: Optional[str] = None


class Provided(OscalBaseModel):
    """
    Describes a capability which may be inherited by a leveraging system.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this provided entry elsewhere in this or other OSCAL instances. The locally defined UUID of the provided entry can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Provided Universally Unique Identifier',
    )
    description: str = Field(
        ...,
        description=
        'An implementation statement that describes the aspects of the control or control statement implementation that can be provided to another system leveraging this system.',
        title='Provided Control Implementation Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    remarks: Optional[str] = None


class OperationalStateValidValues(Enum):
    operational = 'operational'
    under_development = 'under-development'
    under_major_modification = 'under-major-modification'
    disposition = 'disposition'
    other = 'other'


class Inherited(OscalBaseModel):
    """
    Describes a control implementation inherited by a leveraging system.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this inherited entry elsewhere in this or other OSCAL instances. The locally defined UUID of the inherited control implementation can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Inherited Universally Unique Identifier',
    )
    provided_uuid: Optional[constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )] = Field(
        None,
        alias='provided-uuid',
        description=
        'A machine-oriented identifier reference to an inherited control implementation that a leveraging system is inheriting from a leveraged system.',
        title='Provided UUID'
    )
    description: str = Field(
        ...,
        description=
        'An implementation statement that describes the aspects of a control or control statement implementation that a leveraging system is inheriting from a leveraged system.',
        title='Inherited Control Implementation Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')


class ImportProfile(OscalBaseModel):
    """
    Used to import the OSCAL profile representing the system's control baseline.
    """

    class Config:
        extra = Extra.forbid

    href: str = Field(
        ...,
        description="A resolvable URL reference to the profile or catalog to use as the system's control baseline.",
        title='Profile Reference'
    )
    remarks: Optional[str] = None


class Export(OscalBaseModel):
    """
    Identifies content intended for external consumption, such as with leveraged organizations.
    """

    class Config:
        extra = Extra.forbid

    description: Optional[str] = Field(
        None,
        description=
        'An implementation statement that describes the aspects of the control or control statement implementation that can be available to another system leveraging this system.',
        title='Control Implementation Export Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    provided: Optional[List[Provided]] = Field(None)
    responsibilities: Optional[List[Responsibility]] = Field(None)
    remarks: Optional[str] = None


class Diagram(OscalBaseModel):
    """
    A graphic that provides a visual representation the system, or some aspect of it.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this diagram elsewhere in this or other OSCAL instances. The locally defined UUID of the diagram can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Diagram ID'
    )
    description: Optional[str] = Field(None, description='A summary of the diagram.', title='Diagram Description')
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    caption: Optional[str] = Field(None, description='A brief caption to annotate the diagram.', title='Caption')
    remarks: Optional[str] = None


class DateDatatype(OscalBaseModel):
    __root__: constr(
        regex=
        r'^(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))?$'
    ) = Field(..., description='A string representing a 24-hour period with an optional timezone.')


class DateAuthorized(OscalBaseModel):
    __root__: DateDatatype = Field(
        ..., description='The date the system received its authorization.', title='System Authorization Date'
    )


class DataFlow(OscalBaseModel):
    """
    A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.
    """

    class Config:
        extra = Extra.forbid

    description: str = Field(..., description="A summary of the system's data flow.", title='Data Flow Description')
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    diagrams: Optional[List[Diagram]] = Field(None)
    remarks: Optional[str] = None


class Categorization(OscalBaseModel):
    """
    A set of information type identifiers qualified by the given identification system used, such as NIST SP 800-60.
    """

    class Config:
        extra = Extra.forbid

    system: Union[AnyUrl, System] = Field(
        ...,
        description='Specifies the information type identification system used.',
        title='Information Type Identification System'
    )
    information_type_ids: Optional[List[constr(regex=r'^\S(.*\S)?$')]] = Field(None, alias='information-type-ids')


class ByComponent(OscalBaseModel):
    """
    Defines how the referenced component implements a set of controls.
    """

    class Config:
        extra = Extra.forbid

    component_uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        alias='component-uuid',
        description='A machine-oriented identifier reference to the component that is implemeting a given control.',
        title='Component Universally Unique Identifier Reference'
    )
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this by-component entry elsewhere in this or other OSCAL instances. The locally defined UUID of the by-component entry can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='By-Component Universally Unique Identifier',
    )
    description: str = Field(
        ...,
        description=
        'An implementation statement that describes how a control or a control statement is implemented within the referenced system component.',
        title='Control Implementation Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    set_parameters: Optional[List[SetParameter]] = Field(None, alias='set-parameters')
    implementation_status: Optional[common.ImplementationStatus] = Field(None, alias='implementation-status')
    export: Optional[Export] = Field(
        None,
        description='Identifies content intended for external consumption, such as with leveraged organizations.',
        title='Export'
    )
    inherited: Optional[List[Inherited]] = Field(None)
    satisfied: Optional[List[Satisfied]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    remarks: Optional[str] = None


class Base(OscalBaseModel):
    __root__: constr(regex=r'^\S(.*\S)?$') = Field(
        ...,
        description='The prescribed base (Confidentiality, Integrity, or Availability) security impact level.',
        title='Base Level (Confidentiality, Integrity, or Availability)'
    )


class AuthorizationBoundary(OscalBaseModel):
    """
    A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.
    """

    class Config:
        extra = Extra.forbid

    description: str = Field(
        ...,
        description="A summary of the system's authorization boundary.",
        title='Authorization Boundary Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    diagrams: Optional[List[Diagram]] = Field(None)
    remarks: Optional[str] = None


class Status1(OscalBaseModel):
    """
    Describes the operational status of the system.
    """

    class Config:
        extra = Extra.forbid

    state: OperationalStateValidValues = Field(..., description='The current operating status.', title='State')
    remarks: Optional[str] = None


class Statement(OscalBaseModel):
    """
    Identifies which statements within a control are addressed.
    """

    class Config:
        extra = Extra.forbid

    statement_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='statement-id',
        description='A human-oriented identifier reference to a control statement.',
        title='Control Statement Reference'
    )
    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this control statement elsewhere in this or other OSCAL instances. The UUID of the control statement in the source OSCAL instance is sufficient to reference the data item locally or globally (e.g., in an imported OSCAL instance).',
        title='Control Statement Reference Universally Unique Identifier'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    by_components: Optional[List[ByComponent]] = Field(None, alias='by-components')
    remarks: Optional[str] = None


class ImplementedRequirement(OscalBaseModel):
    """
    Describes how the system satisfies the requirements of an individual control.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this control requirement elsewhere in this or other OSCAL instances. The locally defined UUID of the control requirement can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Control Requirement Universally Unique Identifier',
    )
    control_id: constr(
        regex=
        r'^[_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][_A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-\.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$'
    ) = Field(
        ...,
        alias='control-id',
        description=
        'A reference to a control with a corresponding id value. When referencing an externally defined control, the Control Identifier Reference must be used in the context of the external / imported OSCAL instance (e.g., uri-reference).',
        title='Control Identifier Reference'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    set_parameters: Optional[List[SetParameter]] = Field(None, alias='set-parameters')
    responsible_roles: Optional[List[common.ResponsibleRole]] = Field(None, alias='responsible-roles')
    statements: Optional[List[Statement]] = Field(None)
    by_components: Optional[List[ByComponent]] = Field(None, alias='by-components')
    remarks: Optional[str] = None


class ControlImplementation(OscalBaseModel):
    """
    Describes how the system satisfies a set of controls.
    """

    class Config:
        extra = Extra.forbid

    description: str = Field(
        ...,
        description=
        'A statement describing important things to know about how this set of control satisfaction documentation is approached.',
        title='Control Implementation Description'
    )
    set_parameters: Optional[List[SetParameter]] = Field(None, alias='set-parameters')
    implemented_requirements: List[ImplementedRequirement] = Field(..., alias='implemented-requirements')


class NetworkArchitecture(OscalBaseModel):
    """
    A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.
    """

    class Config:
        extra = Extra.forbid

    description: str = Field(
        ..., description="A summary of the system's network architecture.", title='Network Architecture Description'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    diagrams: Optional[List[Diagram]] = Field(None)
    remarks: Optional[str] = None


class LeveragedAuthorization(OscalBaseModel):
    """
    A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope and can be used to reference this leveraged authorization elsewhere in this or other OSCAL instances. The locally defined UUID of the leveraged authorization can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Leveraged Authorization Universally Unique Identifier',
    )
    title: str = Field(
        ...,
        description='A human readable name for the leveraged authorization in the context of the system.',
        title='title field'
    )
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    party_uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        alias='party-uuid',
        description='A machine-oriented identifier reference to the party that manages the leveraged system.',
        title='party-uuid field'
    )
    date_authorized: DateAuthorized = Field(..., alias='date-authorized')
    remarks: Optional[str] = None


class SystemImplementation(OscalBaseModel):
    """
    Provides information as to how the system is implemented.
    """

    class Config:
        extra = Extra.forbid

    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    leveraged_authorizations: Optional[List[LeveragedAuthorization]] = Field(None, alias='leveraged-authorizations')
    users: List[common.SystemUser] = Field(...)
    components: List[common.SystemComponent] = Field(...)
    inventory_items: Optional[List[common.InventoryItem]] = Field(None, alias='inventory-items')
    remarks: Optional[str] = None


class Impact(OscalBaseModel):
    """
    The expected level of impact resulting from the described information.
    """

    class Config:
        extra = Extra.forbid

    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    base: Base
    selected: Optional[Selected] = None
    adjustment_justification: Optional[AdjustmentJustification] = Field(None, alias='adjustment-justification')


class InformationType(OscalBaseModel):
    """
    Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
    """

    class Config:
        extra = Extra.forbid

    uuid: Optional[constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )] = Field(
        None,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this information type elsewhere in this or other OSCAL instances. The locally defined UUID of the information type can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance). This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='Information Type Universally Unique Identifier',
    )
    title: str = Field(
        ...,
        description=
        'A human readable name for the information type. This title should be meaningful within the context of the system.',
        title='title field'
    )
    description: str = Field(
        ...,
        description='A summary of how this information type is used within the system.',
        title='Information Type Description'
    )
    categorizations: Optional[List[Categorization]] = Field(None)
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    confidentiality_impact: Optional[Impact] = Field(None, alias='confidentiality-impact')
    integrity_impact: Optional[Impact] = Field(None, alias='integrity-impact')
    availability_impact: Optional[Impact] = Field(None, alias='availability-impact')


class SystemInformation(OscalBaseModel):
    """
    Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.
    """

    class Config:
        extra = Extra.forbid

    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    information_types: List[InformationType] = Field(..., alias='information-types')


class SystemCharacteristics(OscalBaseModel):
    """
    Contains the characteristics of the system, such as its name, purpose, and security impact level.
    """

    class Config:
        extra = Extra.forbid

    system_ids: List[common.SystemId] = Field(..., alias='system-ids')
    system_name: constr(
        regex=r'^\S(.*\S)?$'
    ) = Field(..., alias='system-name', description='The full name of the system.', title='System Name - Full')
    system_name_short: Optional[constr(regex=r'^\S(.*\S)?$')] = Field(
        None,
        alias='system-name-short',
        description=
        'A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.',
        title='System Name - Short'
    )
    description: str = Field(..., description='A summary of the system.', title='System Description')
    props: Optional[List[common.Property]] = Field(None)
    links: Optional[List[common.Link]] = Field(None)
    date_authorized: Optional[DateAuthorized] = Field(None, alias='date-authorized')
    security_sensitivity_level: Optional[constr(regex=r'^\S(.*\S)?$')] = Field(
        None,
        alias='security-sensitivity-level',
        description='The overall information system sensitivity categorization, such as defined by FIPS-199.',
        title='Security Sensitivity Level'
    )
    system_information: SystemInformation = Field(..., alias='system-information')
    security_impact_level: Optional[SecurityImpactLevel] = Field(None, alias='security-impact-level')
    status: Status1
    authorization_boundary: AuthorizationBoundary = Field(..., alias='authorization-boundary')
    network_architecture: Optional[NetworkArchitecture] = Field(None, alias='network-architecture')
    data_flow: Optional[DataFlow] = Field(None, alias='data-flow')
    responsible_parties: Optional[List[common.ResponsibleParty]] = Field(None, alias='responsible-parties')
    remarks: Optional[str] = None


class SystemSecurityPlan(OscalBaseModel):
    """
    A system security plan, such as those described in NIST SP 800-18.
    """

    class Config:
        extra = Extra.forbid

    uuid: constr(
        regex=r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description=
        'A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this system security plan (SSP) elsewhere in this or other OSCAL instances. The locally defined UUID of the SSP can be used to reference the data item locally or globally (e.g., in an imported OSCAL instance).This UUID should be assigned per-subject, which means it should be consistently used to identify the same subject across revisions of the document.',
        title='System Security Plan Universally Unique Identifier',
    )
    metadata: common.Metadata
    import_profile: ImportProfile = Field(..., alias='import-profile')
    system_characteristics: SystemCharacteristics = Field(..., alias='system-characteristics')
    system_implementation: SystemImplementation = Field(..., alias='system-implementation')
    control_implementation: ControlImplementation = Field(..., alias='control-implementation')
    back_matter: Optional[common.BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    system_security_plan: SystemSecurityPlan = Field(..., alias='system-security-plan')
