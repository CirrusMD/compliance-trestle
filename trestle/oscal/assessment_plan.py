# modified by fix_any.py
# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# generated by datamodel-codegen:
#   filename:  oscal_assessment-plan_schema.json
#   timestamp: 2020-10-14T00:53:58+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, EmailStr, Field, conint, constr

from trestle.core.base_model import OscalBaseModel


class Prose(OscalBaseModel):
    __root__: str


class Link(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    rel: Optional[str] = Field(
        None,
        description="Describes the type of relationship provided by the link. This can be an indicator of the link's purpose.",
        title='Relation',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    text: str


class Published(OscalBaseModel):
    __root__: datetime


class LastModified(OscalBaseModel):
    __root__: datetime


class Version(OscalBaseModel):
    __root__: str


class OscalVersion(OscalBaseModel):
    __root__: str


class DocId(OscalBaseModel):
    type: str = Field(..., description='Qualifies the kind of document identifier.')
    identifier: str


class Prop(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    ns: Optional[str] = Field(
        None, description='A namespace qualifying the name.', title='Namespace'
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='Indicating the type or classification of the containing object',
        title='Class',
    )
    value: str


class LocationUuid(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class Type(Enum):
    person = 'person'
    organization = 'organization'


class PartyUuid(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class ExternalId(OscalBaseModel):
    type: str = Field(
        ...,
        description='Indicating the type of identifier, address, email or other data item.',
        title='Type',
    )
    id: str


class MemberOfOrganization(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class PartyName(OscalBaseModel):
    __root__: str


class ShortName(OscalBaseModel):
    __root__: str


class AddrLine(OscalBaseModel):
    __root__: str


class City(OscalBaseModel):
    __root__: str


class State(OscalBaseModel):
    __root__: str


class PostalCode(OscalBaseModel):
    __root__: str


class Country(OscalBaseModel):
    __root__: str


class Email(OscalBaseModel):
    __root__: EmailStr


class Phone(OscalBaseModel):
    type: Optional[str] = Field(None, description='Indicates the type of phone number.')
    number: str


class Url(OscalBaseModel):
    __root__: AnyUrl


class Desc(OscalBaseModel):
    __root__: str


class Text(OscalBaseModel):
    __root__: str


class Biblio(OscalBaseModel):
    pass


class Citation(OscalBaseModel):
    text: Text
    properties: Optional[List[Prop]] = None
    biblio: Optional[Biblio] = None


class Hash(OscalBaseModel):
    algorithm: str = Field(
        ..., description='Method by which a hash is derived', title='Hash algorithm'
    )
    value: str


class Title(OscalBaseModel):
    __root__: str


class Base64(OscalBaseModel):
    filename: Optional[str] = Field(
        None,
        description='Name of the file before it was encoded as Base64 to be embedded in a resource. This is the name that will be assigned to the file when the file is decoded.',
        title='File Name',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    value: str


class Description(OscalBaseModel):
    __root__: str


class Remarks(OscalBaseModel):
    __root__: str


class State1(Enum):
    operational = 'operational'
    under_development = 'under-development'
    under_major_modification = 'under-major-modification'
    disposition = 'disposition'
    other = 'other'


class Status(OscalBaseModel):
    state: State1 = Field(
        ..., description='The current operating status.', title='State'
    )
    remarks: Optional[Remarks] = None


class RoleId(OscalBaseModel):
    __root__: str


class FunctionPerformed(OscalBaseModel):
    __root__: str


class Transport(Enum):
    TCP = 'TCP'
    UDP = 'UDP'


class PortRange(OscalBaseModel):
    start: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the starting port number in a port range',
        title='Start',
    )
    end: Optional[conint(ge=0, multiple_of=1)] = Field(
        None,
        description='Indicates the ending port number in a port range',
        title='End',
    )
    transport: Optional[Transport] = Field(
        None, description='Indicates the transport type.', title='Transport'
    )


class Purpose(OscalBaseModel):
    __root__: str


class ImportSsp(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    remarks: Optional[Remarks] = None


class Protocol(OscalBaseModel):
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    name: str = Field(..., description='The short name of the protocol (e.g., TLS).')
    title: Optional[Title] = None
    port_ranges: Optional[List[PortRange]] = Field(None, alias='port-ranges')


class AuthorizedPrivilege(OscalBaseModel):
    title: Title
    description: Optional[Description] = None
    functions_performed: List[FunctionPerformed] = Field(
        ..., alias='functions-performed'
    )


class Address(OscalBaseModel):
    type: Optional[str] = Field(None, description='Indicates the type of address.')
    postal_address: Optional[List[AddrLine]] = Field(None, alias='postal-address')
    city: Optional[City] = None
    state: Optional[State] = None
    postal_code: Optional[PostalCode] = Field(None, alias='postal-code')
    country: Optional[Country] = None


class Rlink(OscalBaseModel):
    href: str = Field(
        ...,
        description='A link to a document or document fragment (actual, nominal or projected)',
        title='hypertext reference',
    )
    media_type: Optional[str] = Field(
        None,
        alias='media-type',
        description='Describes the media type of the linked resource',
        title='Media type',
    )
    hashes: Optional[List[Hash]] = None


class Annotation(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    ns: Optional[str] = Field(
        None, description='A namespace qualifying the name.', title='Namespace'
    )
    value: Optional[str] = Field(
        None, description='Indicates the value of the characteristic.', title='Value'
    )
    remarks: Optional[Remarks] = None


class Revision(OscalBaseModel):
    title: Optional[Title] = None
    published: Optional[Published] = None
    last_modified: Optional[LastModified] = Field(None, alias='last-modified')
    version: Optional[Version] = None
    oscal_version: Optional[OscalVersion] = Field(None, alias='oscal-version')
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class Part(OscalBaseModel):
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    ns: Optional[str] = Field(
        None, description='A namespace qualifying the name.', title='Namespace'
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='Indicating the type or classification of the containing object',
        title='Class',
    )
    title: Optional[Title] = None
    properties: Optional[List[Prop]] = None
    prose: Optional[Prose] = None
    parts: Optional[List[Part]] = None
    links: Optional[List[Link]] = None


class ActivityUuid(OscalBaseModel):
    __root__: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    )


class End(OscalBaseModel):
    __root__: datetime


class Start(OscalBaseModel):
    __root__: datetime


class Sequence(OscalBaseModel):
    __root__: int


class CompareTo(OscalBaseModel):
    __root__: str


class Origination(OscalBaseModel):
    title: Title
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None


class All(OscalBaseModel):
    __root__: str


class SubjectReference(OscalBaseModel):
    uuid_ref: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        alias='uuid-ref',
        description="A pointer to a component, inventory-item, location, party, user, or resource using it's UUID.",
        title='UUID Reference',
    )
    type: str = Field(
        ...,
        description='Indicating the type of identifier, address, email or other data item.',
        title='Type',
    )
    title: Optional[Title] = None
    props: Optional[List[Prop]] = None


class AssessmentMethod(OscalBaseModel):
    method_uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        alias='method-uuid',
        description='Identifies the assessment method.',
        title='Method ID',
    )
    STRVALUE: str


class ExcludeObjective(OscalBaseModel):
    objective_id: str = Field(
        ...,
        alias='objective-id',
        description='Points to an assessment objective.',
        title='Objective ID',
    )
    STRVALUE: str


class IncludeObjective(OscalBaseModel):
    objective_id: str = Field(
        ...,
        alias='objective-id',
        description='Points to an assessment objective.',
        title='Objective ID',
    )
    STRVALUE: str


class ExcludeControl(OscalBaseModel):
    control_id: str = Field(
        ...,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    STRVALUE: str


class IncludeControl(OscalBaseModel):
    control_id: str = Field(
        ...,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    STRVALUE: str


class Objective(OscalBaseModel):
    id: str = Field(
        ...,
        description='Unique identifier of the containing object',
        title='Identifier',
    )
    control_id: str = Field(
        ...,
        alias='control-id',
        description='A reference to a control identifier.',
        title='Control Identifier Reference',
    )
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    part: Part
    methods: Optional[List[AssessmentMethod]] = None
    remarks: Optional[Remarks] = None


class User(OscalBaseModel):
    title: Optional[Title] = None
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    role_ids: List[RoleId] = Field(..., alias='role-ids')
    authorized_privileges: Optional[List[AuthorizedPrivilege]] = Field(
        None, alias='authorized-privileges'
    )
    remarks: Optional[Remarks] = None


class Party(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    type: Type = Field(
        ...,
        description='A category describing the kind of party the object describes.',
        title='Party Type',
    )
    party_name: PartyName = Field(..., alias='party-name')
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    external_ids: Optional[List[ExternalId]] = Field(None, alias='external-ids')
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    addresses: Optional[List[Address]] = None
    email_addresses: Optional[List[Email]] = Field(None, alias='email-addresses')
    telephone_numbers: Optional[List[Phone]] = Field(None, alias='telephone-numbers')
    member_of_organizations: Optional[List[MemberOfOrganization]] = Field(
        None, alias='member-of-organizations'
    )
    location_uuids: Optional[List[LocationUuid]] = Field(None, alias='location-uuids')
    remarks: Optional[Remarks] = None


class Location(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    address: Address
    email_addresses: Optional[List[Email]] = Field(None, alias='email-addresses')
    telephone_numbers: Optional[List[Phone]] = Field(None, alias='telephone-numbers')
    URLs: Optional[List[Url]] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class ExcludeActivity(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    role_ids: Optional[List[RoleId]] = Field(None, alias='role-ids')
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    location_uuids: Optional[List[LocationUuid]] = Field(None, alias='location-uuids')
    compare_to: Optional[CompareTo] = Field(None, alias='compare-to')
    remarks: Optional[Remarks] = None


class IncludeActivity(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    role_ids: Optional[List[RoleId]] = Field(None, alias='role-ids')
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    location_uuids: Optional[List[LocationUuid]] = Field(None, alias='location-uuids')
    compare_to: Optional[CompareTo] = Field(None, alias='compare-to')
    remarks: Optional[Remarks] = None


class Task(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    start: Optional[Start] = None
    end: Optional[End] = None
    activity_uuids: Optional[List[ActivityUuid]] = Field(None, alias='activity-uuids')
    role_ids: Optional[List[RoleId]] = Field(None, alias='role-ids')
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    location_uuids: Optional[List[LocationUuid]] = Field(None, alias='location-uuids')
    compare_to: Optional[CompareTo] = Field(None, alias='compare-to')
    remarks: Optional[Remarks] = None


class TestStep(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    sequence: Optional[Sequence] = None
    description: Description
    role_ids: Optional[List[RoleId]] = Field(None, alias='role-ids')
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    compare_to: Optional[CompareTo] = Field(None, alias='compare-to')
    remarks: Optional[Remarks] = None


class ExcludeSubject(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='Indicating the type or classification of the containing object',
        title='Class',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    all: Optional[All] = None
    subject_references: Optional[List[SubjectReference]] = Field(
        None, alias='subject-references'
    )
    remarks: Optional[Remarks] = None


class IncludeSubject(OscalBaseModel):
    name: str = Field(
        ...,
        description='Identifying the purpose and intended use of the property, part or other object.',
        title='Name',
    )
    class_: Optional[str] = Field(
        None,
        alias='class',
        description='Indicating the type or classification of the containing object',
        title='Class',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    all: Optional[All] = None
    subject_references: Optional[List[SubjectReference]] = Field(
        None, alias='subject-references'
    )
    remarks: Optional[Remarks] = None


class Method(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    part: Part
    remarks: Optional[Remarks] = None


class ControlObjectives(OscalBaseModel):
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    all: Optional[All] = None
    include_objectives: Optional[List[IncludeObjective]] = Field(
        None, alias='include-objectives'
    )
    exclude_objectives: Optional[List[ExcludeObjective]] = Field(
        None, alias='exclude-objectives'
    )
    remarks: Optional[Remarks] = None


class Controls(OscalBaseModel):
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    all: Optional[All] = None
    include_controls: Optional[List[IncludeControl]] = Field(
        None, alias='include-controls'
    )
    exclude_controls: Optional[List[ExcludeControl]] = Field(
        None, alias='exclude-controls'
    )
    remarks: Optional[Remarks] = None


class ResponsibleRole(OscalBaseModel):
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    party_uuids: Optional[List[PartyUuid]] = Field(None, alias='party-uuids')
    remarks: Optional[Remarks] = None


class ResponsibleParty(OscalBaseModel):
    party_uuids: List[PartyUuid] = Field(..., alias='party-uuids')
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class Role(OscalBaseModel):
    id: str = Field(
        ...,
        description='Unique identifier of the containing object',
        title='Identifier',
    )
    title: Title
    short_name: Optional[ShortName] = Field(None, alias='short-name')
    desc: Optional[Desc] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    remarks: Optional[Remarks] = None


class Resource(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    desc: Optional[Desc] = None
    properties: Optional[List[Prop]] = None
    document_ids: Optional[List[DocId]] = Field(None, alias='document-ids')
    citation: Optional[Citation] = None
    rlinks: Optional[List[Rlink]] = None
    attachments: Optional[List[Base64]] = None
    remarks: Optional[Remarks] = None


class Objectives(OscalBaseModel):
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    control_group: List[Controls] = Field(..., alias='control-group')
    control_objective_group: Optional[List[ControlObjectives]] = Field(
        None, alias='control-objective-group'
    )
    objectives: Optional[Union[Objective, Objective]] = None
    method_definitions: Optional[List[Method]] = Field(None, alias='method-definitions')
    remarks: Optional[Remarks] = None


class Metadata(OscalBaseModel):
    title: Title
    published: Optional[Published] = None
    last_modified: LastModified = Field(..., alias='last-modified')
    version: Version
    oscal_version: OscalVersion = Field(..., alias='oscal-version')
    revision_history: Optional[List[Revision]] = Field(None, alias='revision-history')
    document_ids: Optional[List[DocId]] = Field(None, alias='document-ids')
    properties: Optional[List[Prop]] = None
    links: Optional[List[Link]] = None
    roles: Optional[List[Role]] = None
    locations: Optional[List[Location]] = None
    parties: Optional[List[Party]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class Schedule(OscalBaseModel):
    uuid: Optional[
        constr(
            regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
        )
    ] = Field(
        None,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    tasks: List[Task]


class TestMethod(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    title: Optional[Title] = None
    description: Optional[Description] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    test_steps: Optional[List[TestStep]] = Field(None, alias='test-steps')
    compare_to: Optional[CompareTo] = Field(None, alias='compare-to')
    remarks: Optional[Remarks] = None


class Component(OscalBaseModel):
    component_type: str = Field(
        ...,
        alias='component-type',
        description='A category describing the purpose of the component.',
        title='Component Type',
    )
    title: Title
    description: Description
    purpose: Optional[Purpose] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    status: Status
    responsible_roles: Optional[Dict[str, ResponsibleRole]] = Field(None, alias='responsible-roles')
    protocols: Optional[List[Protocol]] = None
    remarks: Optional[Remarks] = None


class BackMatter(OscalBaseModel):
    resources: Optional[List[Resource]] = None


class ImplementedComponent(OscalBaseModel):
    use: Optional[str] = Field(
        None, description='The type of implementation', title='Implementation Use Type'
    )
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    remarks: Optional[Remarks] = None


class InventoryItem(OscalBaseModel):
    asset_id: str = Field(
        ...,
        alias='asset-id',
        description='Organizational asset identifier that is unique in the context of the system. This may be a reference to the identifier used in an asset tracking system or a vulnerability scanning tool.',
        title='Asset Identifier',
    )
    description: Description
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    links: Optional[List[Link]] = None
    responsible_parties: Optional[Dict[str, ResponsibleParty]] = Field(
        None, alias='responsible-parties'
    )
    implemented_components: Optional[Dict[str, ImplementedComponent]] = Field(
        None, alias='implemented-components'
    )
    remarks: Optional[Remarks] = None


class LocalDefinitions(OscalBaseModel):
    components: Optional[Dict[str, Component]] = None
    inventory_items: Optional[Dict[str, InventoryItem]] = Field(None, alias='inventory-items')
    users: Optional[Dict[str, User]] = None
    remarks: Optional[Remarks] = None


class Tools(OscalBaseModel):
    components: Optional[Dict[str, Component]] = None


class AssessmentActivities(OscalBaseModel):
    test_methods: Optional[List[TestMethod]] = Field(None, alias='test-methods')
    schedule: Optional[Schedule] = None
    include_activities: Optional[List[IncludeActivity]] = Field(
        None, alias='include-activities'
    )
    exclude_activities: Optional[List[ExcludeActivity]] = Field(
        None, alias='exclude-activities'
    )
    remarks: Optional[Remarks] = None


class AssessmentSubjects(OscalBaseModel):
    includes: List[IncludeSubject]
    excludes: Optional[List[ExcludeSubject]] = None
    local_definitions: Optional[LocalDefinitions] = Field(
        None, alias='local-definitions'
    )
    remarks: Optional[Remarks] = None


class Assets(OscalBaseModel):
    tools: Optional[Tools] = None
    origination: Optional[Origination] = None
    properties: Optional[List[Prop]] = None
    annotations: Optional[List[Annotation]] = None
    parts: Optional[List[Part]] = None
    remarks: Optional[Remarks] = None


class AssessmentPlan(OscalBaseModel):
    uuid: constr(
        regex='^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$'
    ) = Field(
        ...,
        description='A RFC 4122 version 4 Universally Unique Identifier (UUID) for the containing object.',
        title='Universally Unique Identifier',
    )
    metadata: Metadata
    import_ssp: ImportSsp = Field(..., alias='import-ssp')
    objectives: Objectives
    assessment_subjects: Optional[AssessmentSubjects] = Field(
        None, alias='assessment-subjects'
    )
    assets: Optional[Assets] = None
    assessment_activities: Optional[AssessmentActivities] = Field(
        None, alias='assessment-activities'
    )
    back_matter: Optional[BackMatter] = Field(None, alias='back-matter')


class Model(OscalBaseModel):
    assessment_plan: AssessmentPlan = Field(..., alias='assessment-plan')


Part.update_forward_refs()
